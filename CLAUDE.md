# Claude Code Guidelines for kimyonghee.com

## Bilingual Content Requirements (한/영 콘텐츠 요구사항)

All new content files MUST include both Korean and English versions.

모든 새 콘텐츠 파일은 반드시 한국어와 영어 버전을 모두 포함해야 합니다.

---

### Publications (.md files in `src/content/publications/`)

Required frontmatter fields for bilingual support:

```yaml
---
title: "English title of the paper"
title_ko: "논문의 한국어 제목"  # Optional if paper is in English
authors: ["Kim, Y.", "Author2"]
journal: "Journal Name"
year: 2025
type: "ssci"  # Options: ssci, scopus, kci, conference
status: "published"  # Options: published, working-paper, work-in-progress
category: "Category Name"
volume: 88
pages: "104516"
doi: "10.1016/..."
impact_factor: 13.1
quartile: "Q1"
citations: 0
abstract: "English abstract (1-2 sentences)"
abstract_ko: "한국어 초록 (1-2문장)"  # Required for Korean display
keywords: ["keyword1", "keyword2"]
---
```

### Projects (.md files in `src/content/projects/`)

Required frontmatter fields for bilingual support:

```yaml
---
title: "한국어 프로젝트 제목"
title_en: "English Project Title"
subtitle: "한국어 부제"
subtitle_en: "English Subtitle"
description: "한국어 설명"
description_en: "English description"
category: "Category"
date: "2025-01-01"
tags: ["tag1", "tag2"]
featured: true  # Optional
conference: "한국어 학회명"  # Optional
conference_en: "English Conference Name"  # Optional
---
```

### Blog Posts (.md files in `src/content/blog/`)

Required frontmatter fields:

```yaml
---
title: "Blog Post Title"
excerpt: "Short description for preview"
date: "2025-01-01"
category: "Category"
tags: ["tag1", "tag2"]
image: "/images/blog/image.png"  # Optional
---
```

---

## i18n Implementation Pattern (국제화 구현 패턴)

Use `data-lang` attributes for language switching in Astro components:

```astro
<h2 data-lang="en">English Heading</h2>
<h2 data-lang="ko">한국어 제목</h2>

<p data-lang="en">English paragraph content.</p>
<p data-lang="ko">한국어 단락 내용.</p>

<a href="/link" data-lang="en">View More</a>
<a href="/link" data-lang="ko">더 보기</a>
```

The CSS in `BaseLayout.astro` handles visibility:
- Elements with `data-lang="en"` are shown when `html[data-language="en"]`
- Elements with `data-lang="ko"` are shown when `html[data-language="ko"]`

---

## Google Scholar Data Sync (구글 스칼라 데이터 동기화)

A GitHub Action (`update-scholar.yml`) runs weekly to:
1. Fetch latest citation data from Google Scholar
2. Update `src/data/publications.json`
3. Sync citations to individual `.md` files in `src/content/publications/`

Manual sync: Run `python scripts/update_scholar_data.py`

---

## File Structure Overview

```
src/
├── content/
│   ├── publications/    # Publication .md files (bilingual)
│   ├── projects/        # Project .md files (bilingual)
│   └── blog/            # Blog post .md files
├── data/
│   └── publications.json  # Scholar stats & citation data
├── pages/
│   ├── index.astro        # Homepage (bilingual)
│   ├── research/
│   │   └── publications.astro  # Publications page (bilingual)
│   ├── projects/
│   │   └── index.astro    # Projects page (bilingual)
│   └── blog/
│       └── index.astro    # Blog page (bilingual)
└── layouts/
    └── BaseLayout.astro   # Contains i18n CSS rules
```

---

## Deployment

Push to `main` branch triggers automatic deployment via GitHub Actions.

```bash
git add .
git commit -m "message"
git push origin main
```
