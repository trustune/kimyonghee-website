#!/usr/bin/env python3
"""
Update publication metadata from Google Scholar — SAFE MODE.

Design goals (왜 이렇게 바뀌었나):
- 구글 스콜라는 공식 API가 없어 스크래핑(scholarly)에 의존하며, 클라우드 IP(GitHub
  Actions)에서 자주 차단됩니다. 따라서 "가져오기 실패"는 정상적인 상황으로 간주합니다.
- 이 스크립트는 절대 데이터를 망가뜨리지 않습니다:
  1) 항상 기존 publications.json 을 기준선으로 먼저 읽는다.
  2) 가져온 값이 "타당"할 때만(저자 확인 + 인용수>0 + 기존 대비 급락 아님) 사용한다.
  3) 인용수는 단조 증가만 허용한다(max(기존, 신규)). 잘못 긁힌 낮은 값으로 절대 덮어쓰지 않는다.
  4) 어떤 실패/예외에도 종료코드 0으로 끝내고, 데이터는 손대지 않는다.
- 결과: 스콜라가 차단돼도 사이트의 인용 수치(예: 1,308)는 안전하게 유지되고,
  스콜라가 응답할 때만 갱신된다. "계속 에러"가 사라진다.
"""

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path


def install_scholarly() -> bool:
    try:
        import scholarly  # noqa: F401
        return True
    except ImportError:
        try:
            print("[scholar] installing scholarly...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "scholarly"])
            return True
        except Exception as e:
            print(f"[scholar] could not install scholarly: {e}")
            return False


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


def _try_enable_free_proxies(scholarly_mod) -> None:
    """Best-effort: rotate free proxies to reduce Google blocking. Never fatal."""
    try:
        from scholarly import ProxyGenerator
        pg = ProxyGenerator()
        if pg.FreeProxies():
            scholarly_mod.use_proxy(pg)
            print("[scholar] free-proxy rotation enabled")
    except Exception as e:
        print(f"[scholar] proxy setup skipped ({e}); continuing without proxy")


def get_scholar_data(author_id, max_retries=3, retry_delay_seconds=20, request_delay_seconds=2):
    """Fetch author stats/publications from Google Scholar. Returns dict or None (never raises)."""
    try:
        from scholarly import scholarly
    except Exception as e:
        print(f"[scholar] scholarly unavailable: {e}")
        return None

    _try_enable_free_proxies(scholarly)
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
            time.sleep(retry_delay_seconds * attempt)

    if not author:
        return None

    try:
        stats = {
            "citations": _safe_int(author.get("citedby", 0)),
            "hIndex": _safe_int(author.get("hindex", 0)),
            "i10Index": _safe_int(author.get("i10index", 0)),
        }
        print(f"[scholar] fetched citations={stats['citations']}, h={stats['hIndex']}, i10={stats['i10Index']}")

        publications = []
        raw_publications = author.get("publications", []) or []
        for idx, pub in enumerate(raw_publications, 1):
            try:
                pub_filled = scholarly.fill(pub)
                bib = pub_filled.get("bib", {})
                publications.append({
                    "title": bib.get("title", ""),
                    "citations": _safe_int(pub_filled.get("num_citations", 0), 0),
                    "abstract": bib.get("abstract", ""),
                    "eprint_url": pub_filled.get("eprint_url", ""),
                })
                if request_delay_seconds > 0:
                    time.sleep(request_delay_seconds)
            except Exception as e:
                print(f"[scholar] publication {idx} skipped: {e}")

        citation_graph = []
        for year, count in sorted((author.get("cites_per_year", {}) or {}).items()):
            citation_graph.append({"year": _safe_int(year, 0), "citations": _safe_int(count, 0)})

        return {"stats": stats, "publications": publications, "citation_graph": citation_graph}
    except Exception as e:
        print(f"[scholar] error while parsing author payload: {e}")
        return None


def is_fetch_valid(scholar_data, existing_stats) -> bool:
    """Reject failed or implausible fetches so good data is never overwritten with garbage."""
    if not scholar_data:
        return False
    s = scholar_data.get("stats") or {}
    new_cit = _safe_int(s.get("citations"), 0)
    new_h = _safe_int(s.get("hIndex"), 0)
    if new_cit <= 0 or new_h <= 0:
        print("[safe] reject: fetched citations/h-index are zero (likely a blocked/partial scrape)")
        return False
    prev_cit = _safe_int((existing_stats or {}).get("citations"), 0)
    if prev_cit > 0 and new_cit < prev_cit * 0.6:
        print(f"[safe] reject: fetched citations {new_cit} far below known {prev_cit} (likely bad scrape)")
        return False
    return True


def merge_safely(existing_data, scholar_data):
    """Monotonic, non-destructive merge. Citation counts never decrease."""
    prev_stats = existing_data.get("scholarStats", {}) or {}
    new_stats = scholar_data["stats"]
    # 단조 증가: 기존보다 낮으면 무시(잘못 긁힌 값 방어)
    merged_stats = {
        "citations": max(_safe_int(prev_stats.get("citations"), 0), _safe_int(new_stats.get("citations"), 0)),
        "hIndex": max(_safe_int(prev_stats.get("hIndex"), 0), _safe_int(new_stats.get("hIndex"), 0)),
        "i10Index": max(_safe_int(prev_stats.get("i10Index"), 0), _safe_int(new_stats.get("i10Index"), 0)),
    }
    existing_data["scholarStats"] = merged_stats

    # citationGraph: 비어있지 않을 때만 교체
    new_graph = scholar_data.get("citation_graph") or []
    if new_graph:
        existing_data["citationGraph"] = new_graph

    # 논문별 인용수: 제목 매칭 후 max(기존, 신규)로만 갱신
    scholar_index = [(normalize_title(p.get("title", "")), p) for p in scholar_data.get("publications", [])]
    updated = 0
    for pub in existing_data.get("publications", []):
        title_norm = normalize_title(pub.get("title", ""))
        if not title_norm:
            continue
        match = None
        for s_norm, s_pub in scholar_index:
            if s_norm and (title_norm == s_norm or title_norm in s_norm or s_norm in title_norm):
                match = s_pub
                break
        if not match:
            continue
        new_c = _safe_int(match.get("citations"), 0)
        cur_c = _safe_int(pub.get("citations"), 0)
        if new_c > cur_c:
            pub["citations"] = new_c
            updated += 1
        if not pub.get("abstract") and match.get("abstract"):
            sent = match["abstract"].split(". ")[:2]
            ab = ". ".join(sent).strip()
            if ab and not ab.endswith("."):
                ab += "."
            pub["abstract"] = ab
        if match.get("eprint_url") and not pub.get("pdf"):
            pub["pdf"] = match["eprint_url"]
    print(f"[merge] per-paper citations updated: {updated}")
    return existing_data


def update_md_files(publications, md_dir: Path):
    updated = 0
    for pub in publications:
        pub_id = pub.get("id", "")
        if not pub_id:
            continue
        md_file = md_dir / f"{pub_id}.md"
        if not md_file.exists():
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
            new_content = re.sub(
                r"^(citations:\s*)(\d+)(.*)$",
                f"\\g<1>{_safe_int(pub.get('citations'), 0)}\\g<3>",
                content, flags=re.MULTILINE,
            )
            if new_content != content:
                md_file.write_text(new_content, encoding="utf-8")
                updated += 1
        except Exception as e:
            print(f"[update] failed to update {md_file.name}: {e}")
    print(f"[update] markdown files updated: {updated}")


def main():
    print("=" * 60)
    print("Google Scholar update — SAFE MODE")
    print("=" * 60)

    project_root = Path(__file__).resolve().parent.parent
    json_path = project_root / "src" / "data" / "publications.json"
    md_dir = project_root / "src" / "content" / "publications"

    if not json_path.exists():
        print(f"[safe] {json_path} missing; nothing to do")
        return

    # 1) 기준선: 기존 데이터를 먼저 읽는다.
    try:
        existing_data = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[safe] cannot read existing data ({e}); aborting without changes")
        return
    existing_stats = existing_data.get("scholarStats", {})
    print(f"[safe] baseline citations={existing_stats.get('citations')}, h={existing_stats.get('hIndex')}")

    if not install_scholarly():
        print("[safe] scholarly not available; keeping last-good data, no changes")
        return

    # 2) 가져오기 (실패해도 None 반환, 예외 없음)
    scholar_data = get_scholar_data(
        author_id=os.getenv("SCHOLAR_AUTHOR_ID", "semkeskAAAAJ"),
        max_retries=_safe_int(os.getenv("SCHOLAR_MAX_RETRIES", "3"), 3),
        retry_delay_seconds=_safe_int(os.getenv("SCHOLAR_RETRY_DELAY_SECONDS", "20"), 20),
        request_delay_seconds=_safe_int(os.getenv("SCHOLAR_REQUEST_DELAY_SECONDS", "2"), 2),
    )

    # 3) 검증: 타당하지 않으면 데이터 보존 후 정상 종료
    if not is_fetch_valid(scholar_data, existing_stats):
        print("[safe] no valid Scholar data this run — keeping last-good data unchanged. (정상)")
        return

    # 4) 안전 병합(단조 증가) 후 기록
    merged = merge_safely(existing_data, scholar_data)
    try:
        json_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except Exception as e:
        print(f"[safe] write failed ({e}); leaving previous file intact")
        return
    if md_dir.exists():
        update_md_files(merged.get("publications", []), md_dir)

    s = merged["scholarStats"]
    print(f"[done] citations={s['citations']}, h={s['hIndex']}, i10={s['i10Index']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # 어떤 예외도 빌드/배포를 막지 않는다. 데이터는 위에서 이미 보존됨.
        print(f"[safe] unexpected error ({e}); exiting 0 without breaking anything")
    sys.exit(0)
