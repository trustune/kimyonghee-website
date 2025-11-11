# 김용희 웹사이트 배포 가이드

이 문서는 kimyonghee-website 프로젝트의 업데이트 내역과 사용법을 정리합니다.

## 📋 목차
- [프로젝트 개요](#프로젝트-개요)
- [완료된 작업](#완료된-작업)
- [생성된 컴포넌트](#생성된-컴포넌트)
- [적용된 페이지](#적용된-페이지)
- [배포 방법](#배포-방법)
- [주요 파일 위치](#주요-파일-위치)

---

## 프로젝트 개요

**프로젝트명:** kimyonghee-website
**기술 스택:** Astro 5.12.3, Tailwind CSS 4.1.17
**목적:** 김용희 교수 학술 웹사이트
**언어:** 한국어 + 영어 (이중언어)

---

## 완료된 작업

### 1. 이미지 최적화 ✅
- **도구:** Sharp
- **결과:** 28개 이미지 최적화 (10.70MB → 3.74MB, 65.1% 절감)
- **형식:** WebP 변환 + 반응형 크기 생성 (400w, 800w, 1200w, 1600w)
- **스크립트:** `/scripts/optimize-images.mjs`

### 2. Astro 설정 완료 ✅
- MDX 통합
- Sitemap 생성 (`sitemap-index.xml`)
- Sharp 이미지 서비스 설정
- RSS 피드 생성

### 3. 컴포넌트 라이브러리 구축 ✅

#### 생성된 9개 컴포넌트:

| 컴포넌트 | 위치 | 용도 | 적용 페이지 |
|---------|------|------|------------|
| **Badge** | `src/components/Badge.astro` | 태그, 출판 유형, 지표 표시 | publications, media, blog, research/[id] |
| **StatItem** | `src/components/StatItem.astro` | 통계 수치 표시 | publications, media |
| **PublicationCard** | `src/components/PublicationCard.astro` | 논문 카드 (3 variants) | publications |
| **BlogCard** | `src/components/BlogCard.astro` | 블로그 포스트 카드 | blog/index |
| **ArticleCard** | `src/components/ArticleCard.astro` | 미디어 기고문 카드 | media |
| **SocialShare** | `src/components/SocialShare.astro` | 소셜 공유 버튼 | blog/[slug], research/[id] |
| **DarkModeToggle** | `src/components/DarkModeToggle.astro` | 다크 모드 토글 | BaseLayout (전역) |
| **Comments** | `src/components/Comments.astro` | Giscus 댓글 시스템 | blog/[slug] |
| **Analytics** | `src/components/Analytics.astro` | Plausible Analytics | BaseLayout (전역) |

### 4. 페이지 리팩토링 ✅

#### 적용된 페이지:

**`src/pages/research/publications.astro`**
- ✅ PublicationCard 컴포넌트 사용 (full variant)
- ✅ StatItem 컴포넌트로 Google Scholar 통계 표시
- ✅ Badge 컴포넌트로 논문 유형/지표 표시
- **개선:** 약 200줄 코드 감소, 일관된 디자인

**`src/pages/blog/index.astro`**
- ✅ BlogCard 컴포넌트 사용
- ✅ 검색 및 태그 필터링 기능 유지
- **개선:** 카드 디자인 일관성, 유지보수 용이성

**`src/pages/media.astro`**
- ✅ ArticleCard 컴포넌트 사용 (full variant)
- ✅ StatItem 컴포넌트로 통계 표시
- **개선:** 약 80줄 코드 감소

**`src/pages/blog/[slug].astro`**
- ✅ SocialShare 컴포넌트 추가 (Twitter, Facebook, LinkedIn)
- ✅ Comments 컴포넌트 추가 (Giscus)
- ✅ Badge 컴포넌트로 태그 표시
- **개선:** 소셜 공유 및 댓글 기능 강화

**`src/pages/research/[id].astro`**
- ✅ SocialShare 컴포넌트 추가
- ✅ Badge 컴포넌트 사용
- **개선:** 논문 공유 기능 추가

### 5. 다크 모드 구현 ✅
- LocalStorage 기반 persistent theme
- CSS 변수로 라이트/다크 테마 지원
- BaseLayout에 DarkModeToggle 통합

### 6. 분석 및 검색 도구 ✅
- **Plausible Analytics** - 프라이버시 친화적 웹 분석
- **Pagefind** (v1.4.0) - 사이트 내 검색 (패키지 설치 완료)
- **404 페이지 개선** - 인라인 검색 기능 포함

### 7. 댓글 시스템 ✅
- **Giscus** (GitHub Discussions 기반)
- blog/[slug].astro에 통합
- 설정 필요: GitHub repository ID, category ID

---

## 생성된 컴포넌트 상세

### Badge 컴포넌트

**Props:**
```typescript
interface Props {
  variant?: 'ssci' | 'scie' | 'scopus' | 'if' | 'citations' |
            'wip' | 'working' | 'opinion' | 'editorial' |
            'category' | 'tag' | 'default';
  text: string;
  rounded?: 'small' | 'medium' | 'full';
  size?: 'small' | 'medium' | 'large';
}
```

**사용 예시:**
```astro
<Badge text="SSCI" variant="ssci" />
<Badge text="Impact Factor 3.5" variant="if" size="large" />
<Badge text="127 citations" variant="citations" />
```

### PublicationCard 컴포넌트

**Variants:** `full` (기본값), `compact`, `list`

**사용 예시:**
```astro
<PublicationCard
  publication={pub}
  variant="full"
  showAbstract={true}
  showBadges={true}
  showLinks={true}
/>
```

### SocialShare 컴포넌트

**플랫폼:** Twitter, Facebook, LinkedIn

**사용 예시:**
```astro
<SocialShare
  title={post.title}
  url={currentUrl}
/>
```

### Comments 컴포넌트 (Giscus)

**현재 설정 (적용 완료):**
```astro
<Comments
  repo="trustune/kimyonghee-website"
  repoId="R_kgDOQSpBlA"
  category="Announcements"
  categoryId="DIC_kwDOQSpBlM4CXohB"
/>
```

**설정 상태:**
- ✅ GitHub repository: `trustune/kimyonghee-website`
- ✅ Discussions 활성화됨
- ✅ Giscus 앱 설치됨
- ✅ Category: Announcements (관리자 전용)
- ✅ Theme: Preferred color scheme (다크 모드 호환)
- ✅ 모든 블로그 포스트에 댓글 기능 활성화

**댓글 작동 방식:**
1. 방문자가 댓글을 남기면 GitHub OAuth로 인증
2. 댓글은 GitHub Discussions에 자동으로 저장됨
3. Announcements 카테고리를 사용하여 관리자만 새 토론 생성 가능 (스팸 방지)

---

## 배포 방법

### 개발 서버 실행
```bash
npm run dev
```

### 프로덕션 빌드
```bash
npm run build
```
- 빌드 결과: `dist/` 디렉토리
- 24개 페이지 생성
- 빌드 시간: ~80초

### 프로덕션 배포
```bash
rsync -avz --delete dist/ /var/www/kimyonghee.com/public/
```

### 이미지 최적화 (필요 시)
```bash
node scripts/optimize-images.mjs
```

---

## 주요 파일 위치

### 설정 파일
- `astro.config.mjs` - Astro 설정 (MDX, Sitemap, Sharp)
- `tailwind.config.mjs` - Tailwind CSS 설정
- `package.json` - 프로젝트 의존성

### 컴포넌트
- `src/components/` - 모든 재사용 가능한 컴포넌트
- `src/layouts/BaseLayout.astro` - 기본 레이아웃 (Analytics, DarkMode 포함)

### 페이지
- `src/pages/` - 모든 페이지
- `src/pages/research/publications.astro` - 논문 목록
- `src/pages/blog/index.astro` - 블로그 목록
- `src/pages/blog/[slug].astro` - 블로그 상세 (Comments, Share 포함)
- `src/pages/research/[id].astro` - 논문 상세 (Share 포함)
- `src/pages/media.astro` - 미디어 기고문

### 데이터
- `src/data/publications.json` - 논문 데이터
- `src/data/blog.json` - 블로그 포스트 데이터
- `src/data/media.json` - 미디어 기고문 데이터

### 스크립트
- `scripts/optimize-images.mjs` - 이미지 최적화 스크립트

### 문서
- `COMPONENTS_GUIDE.md` - 컴포넌트 상세 사용법
- `DEPLOYMENT_GUIDE.md` - 이 문서

---

## 빌드 결과

### 최종 빌드 통계
```
✓ 24 pages built in 81.75s
✓ Sitemap generated: sitemap-index.xml, sitemap-0.xml
✓ Total size: 17.37MB (이미지 최적화 포함)
```

### 생성된 페이지 (24개)
- 홈페이지 (1)
- About, CV (2)
- 블로그 목록 + 상세 (3)
- 논문 목록 + 상세 15개 (16)
- 미디어 (1)
- 404 페이지 (1)

---

## 다음 단계 (선택사항)

### 즉시 필요한 작업
- [x] **Giscus 설정 완료** ✅ (댓글 기능 활성화됨)
  - Repository: `trustune/kimyonghee-website`
  - Category: Announcements
  - 모든 블로그 포스트에 댓글 기능 활성화
- [x] **Plausible Analytics 설정 완료** ✅
  - 커스텀 스크립트 적용됨 (`pa-oNGrHj6mLCxyqedf0wgS0.js`)

### 향후 개선 사항
- [ ] Pagefind 검색 UI 통합 (현재 패키지만 설치됨)
- [ ] Content Collections 마이그레이션 (JSON → Astro Content)
- [ ] 이미지 lazy loading 최적화
- [ ] PWA 지원 추가
- [ ] 다국어 지원 강화

---

## 문제 해결

### 빌드 경고
```
[WARN] [glob-loader] The base directory "/home/projects/kimyonghee-website/src/content/work/" does not exist.
```
**원인:** Content Collections의 work 디렉토리 미존재
**해결:** 무시 가능 (현재 사용하지 않는 기능)

### npm 보안 취약점
```
3 vulnerabilities (2 moderate, 1 high)
```
**해결방법:**
```bash
npm audit fix
```

---

## 기술 스택 상세

| 카테고리 | 기술 | 버전 |
|---------|------|------|
| Framework | Astro | 5.12.3 |
| Styling | Tailwind CSS | 4.1.17 |
| Typography | @tailwindcss/typography | 0.5.16 |
| Content | MDX | 4.3.1 |
| Images | Sharp | 0.34.5 |
| Search | Pagefind | 1.4.0 |
| RSS | @astrojs/rss | 4.0.12 |
| Sitemap | @astrojs/sitemap | 3.4.1 |
| Analytics | Plausible | - |
| Comments | Giscus | - |

---

## 연락처

**프로젝트 관리자:** 김용희 교수
**이메일:** yhkim1981@sunmoon.ac.kr
**GitHub:** https://github.com/yhkim1981-svg

---

**마지막 업데이트:** 2025-11-10
**배포 버전:** 2.1 (Giscus 댓글 시스템 + Plausible Analytics 완료)
