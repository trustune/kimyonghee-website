#!/usr/bin/env python3
"""
Google Scholar 크롤링 스크립트
논문 제목, 인용 수, 연도, abstract 등을 자동으로 가져와서 publications.json 업데이트
"""

import json
import re
import time
from pathlib import Path

def install_scholarly():
    """scholarly 라이브러리 설치"""
    import subprocess
    try:
        import scholarly
        print("✓ scholarly 라이브러리가 이미 설치되어 있습니다.")
    except ImportError:
        print("scholarly 라이브러리를 설치합니다...")
        subprocess.check_call(["pip", "install", "scholarly"])
        print("✓ scholarly 설치 완료")

def get_scholar_data(author_id="semkeskAAAAJ"):
    """Google Scholar에서 저자 정보 및 논문 데이터 가져오기"""
    from scholarly import scholarly

    print(f"\n📚 Google Scholar 프로필 검색 중: {author_id}")

    try:
        # 저자 프로필 가져오기
        search_query = scholarly.search_author_id(author_id)
        author = scholarly.fill(search_query)

        print(f"✓ 저자: {author.get('name', 'Unknown')}")
        print(f"✓ 소속: {author.get('affiliation', 'Unknown')}")

        # 통계 정보
        stats = {
            'citations': author.get('citedby', 0),
            'hIndex': author.get('hindex', 0),
            'i10Index': author.get('i10index', 0),
        }

        print(f"\n📊 통계:")
        print(f"  - Citations: {stats['citations']}")
        print(f"  - h-index: {stats['hIndex']}")
        print(f"  - i10-index: {stats['i10Index']}")

        # 논문 목록
        publications = []
        print(f"\n📄 논문 정보 수집 중...")

        for idx, pub in enumerate(author.get('publications', []), 1):
            try:
                # 상세 정보 가져오기 (느릴 수 있음)
                pub_filled = scholarly.fill(pub)

                pub_data = {
                    'title': pub_filled.get('bib', {}).get('title', ''),
                    'authors': pub_filled.get('bib', {}).get('author', '').split(' and '),
                    'journal': pub_filled.get('bib', {}).get('venue', ''),
                    'year': int(pub_filled.get('bib', {}).get('pub_year', 0)) if pub_filled.get('bib', {}).get('pub_year') else None,
                    'citations': pub_filled.get('num_citations', 0),
                    'abstract': pub_filled.get('bib', {}).get('abstract', ''),
                    'pub_url': pub_filled.get('pub_url', ''),
                    'eprint_url': pub_filled.get('eprint_url', ''),
                }

                publications.append(pub_data)
                print(f"  {idx}. {pub_data['title'][:60]}... ({pub_data['citations']} citations)")

                # Google Scholar 차단 방지를 위한 지연
                time.sleep(2)

            except Exception as e:
                print(f"  ⚠ 논문 {idx} 처리 실패: {e}")
                continue

        print(f"\n✓ 총 {len(publications)}개 논문 정보 수집 완료")

        # 인용 그래프 데이터 수집
        citation_graph = []
        try:
            cites_per_year = author.get('cites_per_year', {})
            if cites_per_year:
                for year, count in sorted(cites_per_year.items()):
                    citation_graph.append({'year': int(year), 'citations': count})
                print(f"\n📊 인용 그래프 데이터 수집 완료 ({len(citation_graph)}개 연도)")
        except Exception as e:
            print(f"⚠ 인용 그래프 데이터 수집 실패: {e}")

        return {
            'stats': stats,
            'publications': publications,
            'citation_graph': citation_graph
        }

    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return None

def match_and_update_publications(scholar_data, json_path):
    """
    크롤링한 데이터를 기존 publications.json과 매칭하여 업데이트
    """
    print(f"\n📝 publications.json 업데이트 중...")

    # 기존 JSON 읽기
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_pubs = data.get('publications', [])
    scholar_pubs = scholar_data['publications']

    updated_count = 0

    for existing_pub in existing_pubs:
        existing_title = existing_pub.get('title', '').lower().strip()

        # Scholar 데이터에서 매칭되는 논문 찾기 (제목 유사도 기반)
        for scholar_pub in scholar_pubs:
            scholar_title = scholar_pub.get('title', '').lower().strip()

            # 제목이 포함되어 있으면 매칭으로 간주
            if existing_title in scholar_title or scholar_title in existing_title:
                # 인용 수 업데이트
                existing_pub['citations'] = scholar_pub['citations']

                # abstract가 없으면 추가
                if not existing_pub.get('abstract') and scholar_pub.get('abstract'):
                    # abstract를 1-2문장으로 축약
                    abstract_sentences = scholar_pub['abstract'].split('. ')[:2]
                    existing_pub['abstract'] = '. '.join(abstract_sentences).strip()
                    if not existing_pub['abstract'].endswith('.'):
                        existing_pub['abstract'] += '.'

                # PDF URL 업데이트
                if scholar_pub.get('eprint_url') and not existing_pub.get('pdf'):
                    existing_pub['pdf'] = scholar_pub['eprint_url']

                # status 업데이트
                if not existing_pub.get('status'):
                    existing_pub['status'] = 'published'

                updated_count += 1
                print(f"  ✓ 업데이트: {existing_pub['title'][:60]}... ({existing_pub['citations']} citations)")
                break

    # Scholar 통계와 그래프 데이터 추가
    data['scholarStats'] = scholar_data['stats']
    data['citationGraph'] = scholar_data.get('citation_graph', [])

    # JSON 저장
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {updated_count}개 논문 정보 업데이트 완료!")
    print(f"✅ Scholar 통계 업데이트 완료!")
    print(f"📁 저장 위치: {json_path}")

    return updated_count, data.get('publications', [])


def update_md_files(publications, md_dir):
    """
    publications.json의 citations 데이터를 .md 파일에도 동기화
    """
    print(f"\n📝 Markdown 파일 업데이트 중...")

    updated_count = 0

    for pub in publications:
        pub_id = pub.get('id', '')
        citations = pub.get('citations', 0)

        if not pub_id:
            continue

        md_file = md_dir / f"{pub_id}.md"

        if not md_file.exists():
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # frontmatter에서 citations 값 찾기 및 업데이트
            pattern = r'^(citations:\s*)(\d+)(.*)$'
            new_content = re.sub(
                pattern,
                f'\\g<1>{citations}\\g<3>',
                content,
                flags=re.MULTILINE
            )

            if new_content != content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_count += 1
                print(f"  ✓ {pub_id}.md 업데이트 ({citations} citations)")

        except Exception as e:
            print(f"  ⚠ {pub_id}.md 업데이트 실패: {e}")

    print(f"\n✅ {updated_count}개 Markdown 파일 업데이트 완료!")
    return updated_count

def update_scholar_stats(scholar_data, astro_file_path):
    """
    publications.astro 파일의 Scholar 통계 자동 업데이트
    """
    print(f"\n📊 publications.astro의 통계 업데이트 중...")

    with open(astro_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    stats = scholar_data['stats']

    # 통계 섹션 찾기 및 교체
    import re

    pattern = r'const scholarStats = \{[^}]+\};'

    new_stats = f"""const scholarStats = {{
  citations: {stats['citations']},
  citationsSince2020: 957,  // 수동 업데이트 필요
  hIndex: {stats['hIndex']},
  hIndexSince2020: 6,  // 수동 업데이트 필요
  i10Index: {stats['i10Index']},
  i10IndexSince2020: 5,  // 수동 업데이트 필요
  lastUpdated: "November 2025"
}};"""

    content = re.sub(pattern, new_stats, content)

    with open(astro_file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 통계 업데이트 완료!")
    print(f"  - Citations: {stats['citations']}")
    print(f"  - h-index: {stats['hIndex']}")
    print(f"  - i10-index: {stats['i10Index']}")

def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("Google Scholar 크롤링 및 데이터 업데이트")
    print("=" * 60)

    # scholarly 설치 확인
    install_scholarly()

    # 프로젝트 경로 설정
    project_root = Path(__file__).parent.parent
    json_path = project_root / 'src' / 'data' / 'publications.json'
    md_dir = project_root / 'src' / 'content' / 'publications'
    astro_path = project_root / 'src' / 'pages' / 'research' / 'publications.astro'

    print(f"\n📂 프로젝트 경로: {project_root}")
    print(f"📂 JSON 경로: {json_path}")
    print(f"📂 MD 경로: {md_dir}")

    # Google Scholar 데이터 가져오기
    scholar_data = get_scholar_data("semkeskAAAAJ")

    if not scholar_data:
        print("\n❌ Scholar 데이터를 가져오지 못했습니다.")
        return

    # publications.json 업데이트
    _, publications = match_and_update_publications(scholar_data, json_path)

    # .md 파일 citations 동기화
    update_md_files(publications, md_dir)

    # publications.astro 통계 업데이트
    # update_scholar_stats(scholar_data, astro_path)

    print("\n" + "=" * 60)
    print("✅ 모든 업데이트 완료!")
    print("=" * 60)
    print("\n다음 단계:")
    print("  1. src/data/publications.json 확인")
    print("  2. npm run build")
    print("  3. cp -r dist/* /var/www/kimyonghee.com/public/")

if __name__ == "__main__":
    main()
