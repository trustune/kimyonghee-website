# 컴포넌트 사용 가이드 (Components Guide)

이 문서는 kimyonghee-website 프로젝트에 새로 추가된 재사용 가능한 Astro 컴포넌트들의 사용법을 설명합니다.

## 목차
- [Badge](#badge)
- [StatItem](#statitem)
- [PublicationCard](#publicationcard)
- [BlogCard](#blogcard)
- [ArticleCard](#articlecard)
- [SocialShare](#socialshare)
- [DarkModeToggle](#darkmodetoggle)
- [Comments](#comments)
- [Analytics](#analytics)

---

## Badge

**위치:** `src/components/Badge.astro`

**목적:** 태그, 출판물 유형, 지표 등을 표시하는 다양한 스타일의 뱃지

### Props

```typescript
interface Props {
  variant?: 'ssci' | 'scie' | 'scopus' | 'if' | 'citations' | 'wip' |
            'working' | 'opinion' | 'editorial' | 'category' | 'tag' | 'default';
  text: string;
  rounded?: 'small' | 'medium' | 'full';
  size?: 'small' | 'medium' | 'large';
}
```

### 사용 예제

```astro
---
import Badge from '../components/Badge.astro';
---

<!-- 기본 사용 -->
<Badge text="SSCI" variant="ssci" />

<!-- 크기와 둥글기 조절 -->
<Badge text="Impact Factor 3.5" variant="if" size="large" rounded="full" />

<!-- 인용 수 표시 -->
<Badge text="127 citations" variant="citations" />

<!-- Working Paper 상태 -->
<Badge text="Work in Progress" variant="wip" />
```

### 적용 가능한 페이지
- `src/pages/research/publications.astro` - 논문 목록의 뱃지들
- `src/pages/blog/index.astro` - 블로그 태그들
- `src/pages/media.astro` - 기사 카테고리 뱃지들

---

## StatItem

**위치:** `src/components/StatItem.astro`

**목적:** 통계 수치를 일관된 형식으로 표시

### Props

```typescript
interface Props {
  value: string | number;
  label: string;
  sublabel?: string;
  align?: 'left' | 'center' | 'right';
  size?: 'small' | 'medium' | 'large';
}
```

### 사용 예제

```astro
---
import StatItem from '../components/StatItem.astro';
---

<!-- Google Scholar 통계 -->
<div class="stats-grid">
  <StatItem
    value={1176}
    label="Citations"
    sublabel="957 since 2020"
    align="center"
  />
  <StatItem
    value={7}
    label="h-index"
    sublabel="6 since 2020"
    align="center"
  />
</div>
```

### 적용 가능한 페이지
- `src/pages/research/publications.astro` - Google Scholar 통계 섹션
- `src/pages/media.astro` - 기사 통계
- `src/pages/index.astro` - 홈페이지 통계

---

## PublicationCard

**위치:** `src/components/PublicationCard.astro`

**목적:** 연구 논문을 일관된 형식으로 표시

### Props

```typescript
interface Props {
  publication: {
    id?: string;
    title: string;
    authors: string[];
    journal?: string;
    year: number;
    volume?: string;
    issue?: string;
    pages?: string;
    abstract?: string;
    status?: string;
    type?: string;
    impact_factor?: number;
    quartile?: string;
    citations?: number;
    doi?: string;
    pdf?: string;
  };
  variant?: 'full' | 'compact' | 'list';
  showAbstract?: boolean;
  showBadges?: boolean;
  showLinks?: boolean;
}
```

### 사용 예제

```astro
---
import PublicationCard from '../../components/PublicationCard.astro';
import publicationsData from '../../data/publications.json';

const publications = publicationsData.publications || [];
---

<!-- Full 버전 (기본) - 모든 정보 표시 -->
{publications.map(pub => (
  <PublicationCard publication={pub} variant="full" />
))}

<!-- Compact 버전 - 초록 제외 -->
{publications.map(pub => (
  <PublicationCard
    publication={pub}
    variant="compact"
    showAbstract={false}
  />
))}

<!-- List 버전 - 최소 정보만 -->
{publications.map(pub => (
  <PublicationCard
    publication={pub}
    variant="list"
    showBadges={true}
  />
))}
```

### 적용 방법

**publications.astro 리팩토링 예시:**

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import PublicationCard from '../../components/PublicationCard.astro';
import StatItem from '../../components/StatItem.astro';
import publicationsData from '../../data/publications.json';

const publications = publicationsData.publications || [];
const publishedPapers = publications.filter(p => p.status === 'published');
---

<BaseLayout title="Research">
  <div class="research-container">
    <!-- Google Scholar Stats with StatItem -->
    <section class="scholar-stats">
      <StatItem value={1176} label="Citations" sublabel="957 since 2020" />
      <StatItem value={7} label="h-index" sublabel="6 since 2020" />
      <StatItem value={6} label="i10-index" sublabel="5 since 2020" />
    </section>

    <!-- Publications with PublicationCard -->
    <section>
      <h2>Published Papers</h2>
      {publishedPapers.map(pub => (
        <PublicationCard publication={pub} variant="full" />
      ))}
    </section>
  </div>
</BaseLayout>
```

---

## BlogCard

**위치:** `src/components/BlogCard.astro`

**목적:** 블로그 포스트를 카드 형식으로 표시

### Props

```typescript
interface Props {
  post: {
    title: string;
    slug: string;
    date: string;
    excerpt?: string;
    image?: string;
    category?: string;
    tags?: string[];
  };
  showImage?: boolean;
  showExcerpt?: boolean;
  showTags?: boolean;
}
```

### 사용 예제

```astro
---
import BlogCard from '../../components/BlogCard.astro';
import blogData from '../../data/blog.json';

const posts = blogData.posts || [];
---

<!-- 기본 사용 - 모든 요소 표시 -->
<div class="posts-grid">
  {posts.map(post => (
    <BlogCard post={post} />
  ))}
</div>

<!-- 이미지 없이 -->
{posts.map(post => (
  <BlogCard post={post} showImage={false} />
))}

<!-- 최소 정보만 -->
{posts.map(post => (
  <BlogCard
    post={post}
    showImage={false}
    showExcerpt={false}
    showTags={false}
  />
))}
```

### 적용 가능한 페이지
- `src/pages/blog/index.astro` - 블로그 목록
- `src/pages/index.astro` - 홈페이지의 최신 포스트 섹션

---

## ArticleCard

**위치:** `src/components/ArticleCard.astro`

**목적:** 미디어 기고문을 표시

### Props

```typescript
interface Props {
  article: {
    title: string;
    url: string;
    outlet: string;
    date: string;
    type: 'opinion' | 'editorial';
    category?: string;
  };
  variant?: 'full' | 'compact';
}
```

### 사용 예제

```astro
---
import ArticleCard from '../components/ArticleCard.astro';
import media from '../data/media.json';

const articles = media.articles || [];
---

<!-- Full 버전 -->
<div class="article-list">
  {articles.map(article => (
    <ArticleCard article={article} variant="full" />
  ))}
</div>

<!-- Compact 버전 -->
{articles.map(article => (
  <ArticleCard article={article} variant="compact" />
))}
```

### 적용 가능한 페이지
- `src/pages/media.astro` - 미디어 기고문 목록

---

## SocialShare

**위치:** `src/components/SocialShare.astro`

**목적:** 소셜 미디어 공유 버튼

### Props

```typescript
interface Props {
  title: string;
  url: string;
}
```

### 사용 예제

```astro
---
import SocialShare from '../../components/SocialShare.astro';

const pageUrl = `https://kimyonghee.com${Astro.url.pathname}`;
const pageTitle = "My Article Title";
---

<article>
  <h1>{pageTitle}</h1>
  <!-- 콘텐츠 -->

  <!-- 페이지 하단에 공유 버튼 -->
  <SocialShare title={pageTitle} url={pageUrl} />
</article>
```

### 적용 가능한 페이지
- `src/pages/blog/[slug].astro` - 블로그 포스트 상세 페이지
- `src/pages/research/[id].astro` - 논문 상세 페이지

---

## DarkModeToggle

**위치:** `src/components/DarkModeToggle.astro`

**목적:** 다크 모드 토글 버튼

### Props

없음 (props 불필요)

### 사용 예제

```astro
---
import DarkModeToggle from '../components/DarkModeToggle.astro';
---

<nav class="navigation">
  <a href="/">Home</a>
  <a href="/blog">Blog</a>
  <!-- 네비게이션 끝에 다크 모드 토글 추가 -->
  <DarkModeToggle />
</nav>
```

### 현재 적용 상태
- **이미 적용됨:** `src/layouts/BaseLayout.astro` 네비게이션에 통합

---

## Comments

**위치:** `src/components/Comments.astro`

**목적:** Giscus 기반 댓글 시스템 (GitHub Discussions)

### Props

```typescript
interface Props {
  repo?: string;          // GitHub 저장소 (예: "username/repo")
  repoId?: string;        // 저장소 ID
  category?: string;      // Discussion 카테고리
  categoryId?: string;    // 카테고리 ID
}
```

### 설정 방법

1. **GitHub Repository 준비:**
   - Public repository 필요
   - Settings → Features → Discussions 활성화

2. **Giscus 설정:**
   - https://giscus.app 방문
   - Repository 정보 입력하여 설정값 얻기

3. **사용 예제:**

```astro
---
import Comments from '../../components/Comments.astro';
---

<article>
  <h1>Blog Post Title</h1>
  <!-- 콘텐츠 -->

  <!-- 페이지 하단에 댓글 섹션 추가 -->
  <Comments
    repo="yhkim1981-svg/kimyonghee-website"
    repoId="YOUR_REPO_ID"
    category="General"
    categoryId="YOUR_CATEGORY_ID"
  />
</article>
```

### 적용 가능한 페이지
- `src/pages/blog/[slug].astro` - 블로그 포스트 상세 페이지

---

## Analytics

**위치:** `src/components/Analytics.astro`

**목적:** Plausible Analytics (프라이버시 친화적 분석 도구)

### Props

없음 (props 불필요)

### 사용 예제

```astro
---
import Analytics from '../components/Analytics.astro';
---

<html>
<head>
  <title>Page Title</title>
  <!-- head 태그 내에 Analytics 추가 -->
  <Analytics />
</head>
<body>
  <!-- 콘텐츠 -->
</body>
</html>
```

### 현재 적용 상태
- **이미 적용됨:** `src/layouts/BaseLayout.astro` head에 통합
- **설정:** `data-domain="kimyonghee.com"`으로 설정됨

### Plausible 계정 설정

1. https://plausible.io 에서 계정 생성
2. 도메인 추가: `kimyonghee.com`
3. 스크립트가 자동으로 작동함

---

## 다음 단계: 컴포넌트 적용하기

컴포넌트들이 생성되었지만, 아직 기존 페이지에는 적용되지 않았습니다.

### 적용 우선순위

1. **즉시 사용 가능 (이미 적용됨):**
   - ✅ DarkModeToggle (BaseLayout에 통합)
   - ✅ Analytics (BaseLayout에 통합)

2. **적용 권장:**
   - `src/pages/research/publications.astro` → PublicationCard, StatItem, Badge
   - `src/pages/blog/index.astro` → BlogCard
   - `src/pages/media.astro` → ArticleCard, Badge

3. **선택적 적용:**
   - `src/pages/blog/[slug].astro` → SocialShare, Comments
   - `src/pages/research/[id].astro` → SocialShare

### 리팩토링 체크리스트

```markdown
- [ ] publications.astro에 PublicationCard 적용
- [ ] publications.astro에 StatItem 적용
- [ ] blog/index.astro에 BlogCard 적용
- [ ] media.astro에 ArticleCard 적용
- [ ] blog/[slug].astro에 SocialShare 추가
- [ ] blog/[slug].astro에 Comments 추가 (Giscus 설정 후)
```

---

## 스타일 가이드

모든 컴포넌트는 다음 디자인 시스템을 따릅니다:

### 색상 변수
```css
--color-primary: #1e40af;
--color-secondary: #7c3aed;
--color-accent: #2563eb;
--color-text: #1f2937;
--color-text-light: #6b7280;
--color-border: #e5e7eb;
--color-bg: #ffffff;
```

### 다크 모드 색상
```css
.dark {
  --color-text: #f3f4f6;
  --color-text-light: #d1d5db;
  --color-border: #374151;
  --color-bg: #111827;
}
```

### 폰트
- **본문:** 'Paperozi', 'Inter', sans-serif
- **제목:** 'Paperozi', 'Merriweather', serif

---

## 문의 및 지원

컴포넌트 사용 중 문제가 발생하거나 질문이 있으면:
- GitHub Issues 생성
- 이메일: yhkim1981@sunmoon.ac.kr

마지막 업데이트: 2025-11-10
