#!/usr/bin/env python3
"""
Update publication metadata from Google Scholar.
- Updates citation counts in src/data/publications.json
- Syncs citation counts to src/content/publications/*.md frontmatter
- Updates scholarStats and citationGraph in publications.json
"""

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path


def install_scholarly() -> None:
    """Ensure scholarly is installed in the current Python environment."""
    try:
        import scholarly  # noqa: F401
        print("[scholar] scholarly is already installed")
    except ImportError:
        print("[scholar] installing scholarly...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "scholarly"])
        print("[scholar] scholarly installation completed")


def _safe_int(value, default=0):
    try:
        if value is None or value == "":
            return default
        return int(value)
    except Exception:
        return default


def normalize_title(title: str) -> str:
    title = (title or "").lower().strip()
    return re.sub(r"[^a-z0-9]+", "", title)


def get_scholar_data(
    author_id: str = "semkeskAAAAJ",
    max_retries: int = 3,
    retry_delay_seconds: int = 20,
    request_delay_seconds: int = 2,
):
    """Fetch author stats/publications from Google Scholar with retries."""
    from scholarly import scholarly

    print(f"[scholar] fetching profile: {author_id}")

    author = None
    for attempt in range(1, max_retries + 1):
        try:
            search_query = scholarly.search_author_id(author_id)
            author = scholarly.fill(search_query)
            break
        except Exception as e:
            print(f"[scholar] attempt {attempt}/{max_retries} failed: {e}")
            if attempt == max_retries:
                return None
            wait_seconds = retry_delay_seconds * attempt
            print(f"[scholar] retrying in {wait_seconds}s")
            time.sleep(wait_seconds)

    if not author:
        return None

    stats = {
        "citations": _safe_int(author.get("citedby", 0)),
        "hIndex": _safe_int(author.get("hindex", 0)),
        "i10Index": _safe_int(author.get("i10index", 0)),
    }

    print(
        "[scholar] stats "
        f"citations={stats['citations']}, h-index={stats['hIndex']}, i10-index={stats['i10Index']}"
    )

    publications = []
    raw_publications = author.get("publications", [])
    print(f"[scholar] fetching {len(raw_publications)} publication records")

    for idx, pub in enumerate(raw_publications, 1):
        try:
            pub_filled = scholarly.fill(pub)
            bib = pub_filled.get("bib", {})
            pub_data = {
                "title": bib.get("title", ""),
                "authors": (bib.get("author", "") or "").split(" and "),
                "journal": bib.get("venue", ""),
                "year": _safe_int(bib.get("pub_year"), None),
                "citations": _safe_int(pub_filled.get("num_citations", 0), 0),
                "abstract": bib.get("abstract", ""),
                "pub_url": pub_filled.get("pub_url", ""),
                "eprint_url": pub_filled.get("eprint_url", ""),
            }
            publications.append(pub_data)
            print(
                f"[scholar] {idx}/{len(raw_publications)} "
                f"{pub_data['title'][:60]}... ({pub_data['citations']} citations)"
            )
            if request_delay_seconds > 0:
                time.sleep(request_delay_seconds)
        except Exception as e:
            print(f"[scholar] publication {idx} skipped: {e}")

    citation_graph = []
    cites_per_year = author.get("cites_per_year", {}) or {}
    for year, count in sorted(cites_per_year.items()):
        citation_graph.append({"year": _safe_int(year, 0), "citations": _safe_int(count, 0)})

    print(
        f"[scholar] collected {len(publications)} publications, "
        f"{len(citation_graph)} citation-graph points"
    )

    return {
        "stats": stats,
        "publications": publications,
        "citation_graph": citation_graph,
    }


def match_and_update_publications(scholar_data, json_path: Path):
    """Match Scholar publications to local JSON and update fields."""
    print(f"[update] updating {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_pubs = data.get("publications", [])
    scholar_pubs = scholar_data["publications"]

    # Pre-index scholar publications by normalized title for faster matching.
    scholar_index = []
    for pub in scholar_pubs:
        title = pub.get("title", "")
        scholar_index.append((normalize_title(title), pub))

    updated_count = 0

    for existing_pub in existing_pubs:
        existing_title_raw = existing_pub.get("title", "")
        existing_title_norm = normalize_title(existing_title_raw)
        if not existing_title_norm:
            continue

        matched = None
        for scholar_title_norm, scholar_pub in scholar_index:
            if not scholar_title_norm:
                continue
            if (
                existing_title_norm == scholar_title_norm
                or existing_title_norm in scholar_title_norm
                or scholar_title_norm in existing_title_norm
            ):
                matched = scholar_pub
                break

        if not matched:
            continue

        changed = False

        new_citations = _safe_int(matched.get("citations", 0), 0)
        if existing_pub.get("citations") != new_citations:
            existing_pub["citations"] = new_citations
            changed = True

        if not existing_pub.get("abstract") and matched.get("abstract"):
            abstract_sentences = matched["abstract"].split(". ")[:2]
            abstract = ". ".join(abstract_sentences).strip()
            if abstract and not abstract.endswith("."):
                abstract += "."
            existing_pub["abstract"] = abstract
            changed = True

        if matched.get("eprint_url") and not existing_pub.get("pdf"):
            existing_pub["pdf"] = matched["eprint_url"]
            changed = True

        if not existing_pub.get("status"):
            existing_pub["status"] = "published"
            changed = True

        if changed:
            updated_count += 1
            print(
                f"[update] updated: {existing_title_raw[:60]}... "
                f"({existing_pub.get('citations', 0)} citations)"
            )

    data["scholarStats"] = scholar_data["stats"]
    data["citationGraph"] = scholar_data.get("citation_graph", [])

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[update] publications updated: {updated_count}")
    return updated_count, data.get("publications", [])


def update_md_files(publications, md_dir: Path):
    """Sync citations from publications.json to markdown frontmatter."""
    print(f"[update] syncing markdown citations in {md_dir}")

    updated_count = 0
    for pub in publications:
        pub_id = pub.get("id", "")
        citations = _safe_int(pub.get("citations", 0), 0)

        if not pub_id:
            continue

        md_file = md_dir / f"{pub_id}.md"
        if not md_file.exists():
            continue

        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            pattern = r"^(citations:\s*)(\d+)(.*)$"
            new_content = re.sub(
                pattern,
                f"\\g<1>{citations}\\g<3>",
                content,
                flags=re.MULTILINE,
            )

            if new_content != content:
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
                updated_count += 1
                print(f"[update] {md_file.name}: citations={citations}")

        except Exception as e:
            print(f"[update] failed to update {md_file.name}: {e}")

    print(f"[update] markdown files updated: {updated_count}")
    return updated_count


def main():
    print("=" * 60)
    print("Google Scholar update job")
    print("=" * 60)

    install_scholarly()

    project_root = Path(__file__).resolve().parent.parent
    json_path = project_root / "src" / "data" / "publications.json"
    md_dir = project_root / "src" / "content" / "publications"

    if not json_path.exists() or not md_dir.exists():
        print("[error] required paths are missing")
        raise SystemExit(1)

    author_id = os.getenv("SCHOLAR_AUTHOR_ID", "semkeskAAAAJ")
    max_retries = _safe_int(os.getenv("SCHOLAR_MAX_RETRIES", "3"), 3)
    retry_delay = _safe_int(os.getenv("SCHOLAR_RETRY_DELAY_SECONDS", "20"), 20)
    request_delay = _safe_int(os.getenv("SCHOLAR_REQUEST_DELAY_SECONDS", "2"), 2)

    scholar_data = get_scholar_data(
        author_id=author_id,
        max_retries=max_retries,
        retry_delay_seconds=retry_delay,
        request_delay_seconds=request_delay,
    )

    if not scholar_data:
        print("[error] failed to fetch Google Scholar data")
        raise SystemExit(1)

    _, publications = match_and_update_publications(scholar_data, json_path)
    update_md_files(publications, md_dir)

    print("=" * 60)
    print("Scholar update completed")
    print("=" * 60)


if __name__ == "__main__":
    main()
