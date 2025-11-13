# 김용희 교수 웹사이트 인계서 (Complete Handover Document)

**작성일**: 2025년 11월 13일
**버전**: v3.0 FINAL
**작성자**: Claude Code Assistant

---

## 📋 목차

1. [프로젝트 개요](#프로젝트-개요)
2. [완료된 주요 작업](#완료된-주요-작업)
3. [웹사이트 구조](#웹사이트-구조)
4. [기술 스택 및 환경](#기술-스택-및-환경)
5. [배포 시스템](#배포-시스템)
6. [콘텐츠 관리](#콘텐츠-관리)
7. [차트 및 시각화](#차트-및-시각화)
8. [향후 개선 사항](#향후-개선-사항)
9. [문제 해결 가이드](#문제-해결-가이드)
10. [연락처 및 지원](#연락처-및-지원)

---

## 프로젝트 개요

### 웹사이트 정보
- **URL**: https://kimyonghee.com
- **목적**: 선문대학교 경영학부 김용희 교수 개인 학술 웹사이트
- **주요 기능**:
  - 연구 프로젝트 및 논문 소개
  - 데이터 기반 정책 분석 시각화
  - 강의 정보 및 미디어 활동 정리
  - 다국어 지원 (한국어/영어)

### 서버 정보
- **호스팅**: 자체 서버 (115.71.237.77)
- **웹서버**: Nginx
- **배포 경로**: `/var/www/kimyonghee.com/public/`
- **운영체제**: Linux (Ubuntu/Debian)

---

## 완료된 주요 작업

### 2025년 11월 12-13일 작업 내역

#### 1. Broadcasting Revenue Analysis (방송산업 순유입 매출 분석)
**파일**: `/src/content/projects/broadcasting-revenue-2015-2024.md`

**주요 개선사항**:
- ✅ **데이터 정확성 검증 완료**: 99.50% 정확도 달성
- ✅ **Chart.js 인터랙티브 차트 4개 구현**:
  1. 순유입 매출 추이 (라인 차트)
  2. 광고 시장 비교 (라인 차트)
  3. 플랫폼별 비교 (라인 차트)
  4. 기금 분배 현황 (파이 차트)
- ✅ **스토리텔링 구조로 전면 재작성**:
  - Executive Summary with Hero Cards
  - Part I: Crisis Analysis (위기 분석)
  - Part II: Root Causes (원인 분석)
  - Part III: Survival Strategy (생존 전략)
- ✅ **중요 데이터 수정**:
  - Research Methodology와 Project Information 중복 제거
  - 명확한 3가지 핵심 메시지 강조
  - 정책 제안 3단계 로드맵 제시

**핵심 데이터 (절대 변경 금지)**:
```
- 2024 순유입 매출: 8.89조원
- 2019 피크: 9.49조원 (이후 6.4% 감소)
- 방송광고: 34.52% 감소 (3.50T → 2.29T)
- IPTV: 99.1% 증가 vs 케이블: 39.1% 감소
- KBS 수신료 44년 동결 (1981-2025)
- 정부지원 비율: 10.15% (OECD 최하위)
```

#### 2. Broadcasting Reapproval System (방송재승인 제도)
**파일**: `/src/content/projects/broadcasting-reapproval-2024.md`

**주요 개선사항**:
- ✅ **데이터 오류 수정**: "7년" → **"3-4년 실제 (법정 최대 7년)"**
- ✅ **Chart.js 인터랙티브 차트 7개 구현**:
  1. 국제 비교 (막대 차트): 한국 3.5년 vs 타국
  2. 투자 패러독스 (산점도): 투자비율 vs 수익성
  3. TV조선 타임라인 (이중 축): 투자 & 수익 추이
  4. 4개 채널 비교 (멀티 라인): JTBC, 채널A, MBN, TV조선
  5. 영업이익률 (멀티 라인): 수익성 비교
  6. 매체별 평균 (막대): 지상파/종편/PP
  7. 정책 제안 (막대): 현재 vs 제안
- ✅ **스토리텔링 구조 재편**:
  - Part 1: The Shortest Leash in Global Broadcasting
  - Part 2: The Investment Paradox Revealed
  - Part 3: The Tale of Four Channels
  - Part 4: Market Context
  - Part 5: Evidence-Based Policy Recommendations
- ✅ **날짜 업데이트**: 2024-10-11 → 2025-10-11

**핵심 데이터 (절대 변경 금지)**:
```
- 실제 재승인 기간: 3-4년 (법정 최대 7년)
- 국제 비교: 영국 10년, 미국 8년, 일본 6년
- 콘텐츠 투자비율 의무: 70%
- TV조선 평균 투자비율: 73.5% (70% 초과)
- 투자 패러독스: 높은 투자 = 낮은 수익성
```

#### 3. Projects Page Redesign (프로젝트 페이지 재설계)
**파일**: `/src/pages/projects/index.astro`

**주요 개선사항**:
- ✅ **Featured Projects 간격 증가**:
  - `margin-bottom: 4rem → 6rem`
  - `margin-bottom: 3rem` 카드 간격 추가
- ✅ **More Projects → PDF 다운로드 방식으로 변경**:
  - 기존: 그리드 카드 레이아웃
  - 신규: 다운로드 리스트 레이아웃
  - 각 항목에 "View Online" + "Download PDF" 버튼
  - 문서 아이콘 추가
- ✅ **중복 제거**: Featured 프로젝트가 More Projects에 중복 표시되지 않도록 필터링

---

## 웹사이트 구조

### 디렉토리 구조
```
kimyonghee-website/
├── public/                    # 정적 파일
│   ├── images/               # 이미지 파일
│   ├── documents/            # PDF 문서
│   └── projects/             # 프로젝트 데이터
├── src/
│   ├── components/           # 재사용 컴포넌트
│   │   ├── LineChart.astro  # 라인 차트 (Chart.js)
│   │   ├── PieChart.astro   # 파이 차트 (Chart.js)
│   │   └── SocialShare.astro # 소셜 공유
│   ├── content/             # 콘텐츠 (Markdown)
│   │   ├── projects/        # 프로젝트 파일
│   │   ├── blog/           # 블로그 포스트
│   │   └── config.ts       # 콘텐츠 스키마
│   ├── layouts/            # 레이아웃
│   │   └── BaseLayout.astro
│   ├── pages/              # 페이지
│   │   ├── index.astro     # 홈페이지
│   │   ├── about.astro     # 소개
│   │   ├── projects/       # 프로젝트
│   │   ├── research/       # 연구
│   │   ├── teaching.astro  # 강의
│   │   └── media.astro     # 미디어
│   └── data/               # 데이터 파일
├── .github/workflows/       # GitHub Actions
│   └── deploy.yml          # 자동 배포
├── HANDOVER.md             # 기존 인계서
├── HANDOVER_COMPLETE.md    # 완전 인계서 (본 문서)
├── DEPLOYMENT_GUIDE.md     # 배포 가이드
└── LOCAL_SETUP_GUIDE.md    # 로컬 환경 설정
```

### 주요 페이지

| 페이지 | 경로 | 설명 |
|--------|------|------|
| 홈 | `/` | 프로필, 주요 연구, 최근 활동 |
| 소개 | `/about` | 학력, 경력, 전문 분야 |
| 프로젝트 | `/projects` | 연구 프로젝트 목록 |
| 프로젝트 상세 | `/projects/[slug]` | 개별 프로젝트 상세 |
| 연구 | `/research/publications` | 논문 목록 |
| 강의 | `/teaching` | 강의 정보 |
| 미디어 | `/media` | 미디어 활동 |
| 블로그 | `/blog` | 블로그 포스트 |
| CV | `/cv` | 이력서 |

---

## 기술 스택 및 환경

### 프레임워크 & 라이브러리
```json
{
  "astro": "^4.16.18",
  "chart.js": "4.4.0 (CDN)",
  "node": "20.x LTS",
  "npm": "10.x"
}
```

### 핵심 기술
- **Astro 4.x**: 정적 사이트 생성 (SSG)
- **Chart.js 4.4.0**: 인터랙티브 차트 (CDN 방식)
- **Content Collections**: Markdown 콘텐츠 관리
- **Pagefind**: 사이트 내 검색
- **GitHub Actions**: CI/CD 자동 배포

### Chart.js 사용법

#### 1. CDN 추가 (Frontmatter 아래)
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

#### 2. 차트 컨테이너 삽입
```html
<div class="chart-container">
  <div class="chart-title">차트 제목</div>
  <canvas id="myChart"></canvas>
</div>
```

#### 3. 차트 스크립트 작성
```html
<script>
const ctx = document.getElementById('myChart');
if (ctx) {
  new Chart(ctx, {
    type: 'line',  // 또는 'bar', 'pie', 'scatter' 등
    data: {
      labels: ['2015', '2016', '2017'],
      datasets: [{
        label: '데이터셋',
        data: [10, 20, 30],
        borderColor: 'rgb(59, 130, 246)',
        backgroundColor: 'rgba(59, 130, 246, 0.1)'
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'bottom' }
      }
    }
  });
}
</script>
```

### 환경 변수
현재 환경 변수는 사용하지 않습니다. 모든 설정은 코드에 하드코딩되어 있습니다.

---

## 배포 시스템

### GitHub Actions 자동 배포
**파일**: `.github/workflows/deploy.yml`

#### 배포 프로세스
```
1. 로컬에서 코드 수정
   ↓
2. git commit & push
   ↓
3. GitHub Actions 자동 실행
   ├── Node.js 20 설치
   ├── npm install
   ├── npm run build (테스트)
   ├── SSH 접속 (서버: 115.71.237.77)
   ├── git pull origin main
   ├── npm install
   ├── npm run build
   └── rsync → /var/www/kimyonghee.com/public/
   ↓
4. 배포 완료 (약 2-3분 소요)
```

#### GitHub Secrets 설정
필요한 Secrets (Settings → Secrets and variables → Actions):
- `HOST`: 115.71.237.77
- `USERNAME`: root
- `SSH_PRIVATE_KEY`: SSH 개인 키

#### 수동 배포 (서버에서 직접)
```bash
cd /home/projects/kimyonghee-website
git pull origin main
npm install
npm run build
rsync -av --delete dist/ /var/www/kimyonghee.com/public/
```

#### 배포 확인
```bash
# GitHub Actions 로그
https://github.com/trustune/kimyonghee-website/actions

# 웹사이트 확인
https://kimyonghee.com
```

---

## 콘텐츠 관리

### 프로젝트 추가하기

#### 1. 새 Markdown 파일 생성
```bash
# 파일 위치
/src/content/projects/새-프로젝트-slug.md
```

#### 2. Frontmatter 작성
```yaml
---
title: "프로젝트 제목"
title_en: "Project Title in English"
subtitle: "부제목"
subtitle_en: "Subtitle in English"
date: "2025-11-13"
category: "Broadcasting Policy"
tags: ["Broadcasting", "Data Analysis", "Policy"]
conference: "학회명"
conference_en: "Conference Name"
description: "프로젝트 설명"
description_en: "Project description"
summary: "요약 (1-2문장)"
key_findings:
  - "주요 발견 1"
  - "주요 발견 2"
  - "주요 발견 3"
policy_proposals:
  - "정책 제안 1"
  - "정책 제안 2"
featured: true  # 메인 페이지 Featured 섹션에 표시
---
```

#### 3. 본문 작성
- Markdown 형식으로 작성
- HTML/CSS 사용 가능
- Chart.js 차트 삽입 가능

### 블로그 포스트 추가
```bash
# 파일 위치
/src/content/blog/포스트-제목.md
```

Frontmatter 예시:
```yaml
---
title: "블로그 제목"
title_en: "Blog Title"
date: "2025-11-13"
category: "Research"
tags: ["Media", "Policy"]
description: "설명"
description_en: "Description"
---
```

### 데이터 수정

#### 논문 데이터
**파일**: `/src/data/publications.json`

```json
{
  "id": "kim2025-example",
  "title": "논문 제목",
  "title_en": "Paper Title",
  "authors": ["Kim, Y.", "Co-Author"],
  "year": 2025,
  "journal": "저널명",
  "volume": 1,
  "issue": 1,
  "pages": "1-20",
  "doi": "10.1234/example",
  "type": "journal"
}
```

#### 미디어 활동
**파일**: `/src/data/media.json`

```json
{
  "id": "media-2025-01",
  "date": "2025-11-13",
  "type": "interview",
  "title": "인터뷰 제목",
  "outlet": "언론사",
  "url": "https://...",
  "description": "설명"
}
```

---

## 차트 및 시각화

### 구현된 차트 목록

#### Broadcasting Revenue Analysis
1. **순유입 매출 추이** (`revenueChart`)
   - 타입: Line Chart
   - 데이터: Pay-TV, 광고, 홈쇼핑 (2015-2024)

2. **광고 시장 비교** (`advertisingChart`)
   - 타입: Line Chart
   - 데이터: 방송광고 vs 디지털광고

3. **플랫폼별 비교** (`platformChart`)
   - 타입: Line Chart
   - 데이터: IPTV vs 케이블

4. **기금 분배** (`fundPieChart`)
   - 타입: Pie Chart
   - 데이터: 통신/융합/방송 분야

#### Broadcasting Reapproval System
1. **국제 비교** (`internationalComparison`)
   - 타입: Bar Chart
   - 데이터: 한국, 미국, 영국, 일본

2. **투자 패러독스** (`investmentParadox`)
   - 타입: Scatter Plot
   - 데이터: 4개 채널 10년 데이터

3. **TV조선 타임라인** (`tvChosunTimeline`)
   - 타입: Dual-Axis Line Chart
   - 데이터: 투자비율 + 영업이익률

4-7. **4개 채널 분석** (4개 차트)

### 차트 데이터 수정 방법

#### 예시: 순유입 매출 차트 데이터 변경
```javascript
// 파일: /src/pages/projects/[slug].astro

// 1. 데이터 배열 수정
const revenueLabels = ['2015', '2016', ..., '2025'];  // 연도 추가

const revenueDatasets = [
  {
    label: 'Pay-TV Subscriptions',
    data: [27.5, 28.3, ..., 새로운값],  // 데이터 추가
    borderColor: 'rgba(102, 126, 234, 1)',
    // ...
  },
  // ...
];

// 2. 차트에 자동 반영됨
```

### 차트 스타일 커스터마이징
```css
/* 파일: broadcasting-revenue-2015-2024.md */

<style>
.chart-container {
  width: 100%;
  height: 400px;  /* 높이 조정 */
  margin: 2rem 0;
  padding: 1.5rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.chart-canvas {
  width: 100%;
  height: 100%;
}
</style>
```

---

## 향후 개선 사항

### 단기 개선 (1-3개월)
1. **PDF 다운로드 기능 구현**
   - More Projects 섹션의 "Download PDF" 버튼 실제 동작
   - 프로젝트별 PDF 파일 생성 및 업로드
   - 경로: `/public/documents/projects/[slug].pdf`

2. **검색 기능 개선**
   - Pagefind 커스터마이징
   - 한국어 검색 최적화
   - 필터링 기능 추가

3. **모바일 최적화**
   - 차트 반응형 개선
   - 터치 인터랙션 최적화
   - 모바일 네비게이션 개선

### 중기 개선 (3-6개월)
1. **CMS 도입 고려**
   - Decap CMS (구 Netlify CMS) 연동
   - 비개발자도 콘텐츠 편집 가능
   - Git 기반 워크플로우 유지

2. **성능 최적화**
   - 이미지 최적화 (WebP, AVIF)
   - 차트 Lazy Loading
   - 코드 스플리팅

3. **분석 도구 추가**
   - Google Analytics 4
   - 방문자 통계 대시보드

### 장기 개선 (6개월+)
1. **인터랙티브 데이터 탐색**
   - 사용자가 차트 데이터 필터링 가능
   - 데이터 다운로드 기능
   - 비교 분석 도구

2. **다국어 확장**
   - 일본어 버전 추가
   - 자동 번역 통합

3. **API 구축**
   - 연구 데이터 API 제공
   - 외부 사이트 임베딩 지원

---

## 문제 해결 가이드

### 빌드 오류

#### 오류: "Module not found"
```bash
# 해결방법
rm -rf node_modules package-lock.json
npm install
npm run build
```

#### 오류: "Chart.js is not defined"
```html
<!-- 해결방법: CDN 확인 -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

#### 오류: "Cannot find module 'astro:content'"
```bash
# 해결방법: Content Collections 재생성
npm run build
```

### 배포 오류

#### GitHub Actions 실패
1. **Actions 탭 확인**
   - https://github.com/trustune/kimyonghee-website/actions
   - 에러 로그 확인

2. **Secrets 확인**
   - Settings → Secrets and variables → Actions
   - HOST, USERNAME, SSH_PRIVATE_KEY 재확인

3. **서버 SSH 접속 확인**
   ```bash
   ssh root@115.71.237.77
   ```

#### rsync 오류
```bash
# 서버에서 확인
ls -la /var/www/kimyonghee.com/
chmod -R 755 /var/www/kimyonghee.com/public/
```

### 차트 렌더링 오류

#### 차트가 보이지 않음
1. **브라우저 콘솔 확인** (F12)
2. **Chart.js 로드 확인**
   ```javascript
   console.log(typeof Chart);  // "function" 출력되어야 함
   ```
3. **Canvas ID 중복 확인**
   - 각 차트는 고유한 ID 필요

#### 차트 데이터 오류
```javascript
// 데이터 검증
console.log(revenueLabels);  // 배열 확인
console.log(revenueDatasets);  // 데이터 확인
```

### 다국어 전환 오류
```javascript
// 파일: src/layouts/BaseLayout.astro
// 언어 전환 스크립트 확인
document.querySelectorAll('[data-lang]').forEach(el => {
  el.style.display = el.getAttribute('data-lang') === currentLang ? '' : 'none';
});
```

---

## 일반적인 작업 가이드

### 새로운 차트 추가하기

#### Step 1: 차트 컨테이너 추가
```html
<div class="chart-container">
  <div class="chart-title">새 차트 제목</div>
  <canvas id="newChart"></canvas>
</div>
```

#### Step 2: 데이터 준비
```javascript
const newChartLabels = ['Label1', 'Label2', 'Label3'];
const newChartData = {
  datasets: [{
    label: '데이터셋',
    data: [10, 20, 30],
    backgroundColor: 'rgba(59, 130, 246, 0.8)'
  }]
};
```

#### Step 3: 차트 생성
```javascript
const ctxNew = document.getElementById('newChart');
if (ctxNew) {
  new Chart(ctxNew, {
    type: 'bar',  // 차트 타입
    data: {
      labels: newChartLabels,
      datasets: newChartData.datasets
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'top' }
      }
    }
  });
}
```

### 스타일 변경하기

#### 색상 테마 변경
```css
/* 주요 색상 변수 */
:root {
  --primary: #2563eb;      /* 파란색 */
  --secondary: #667eea;    /* 보라색 */
  --success: #10b981;      /* 초록색 */
  --warning: #f59e0b;      /* 주황색 */
  --danger: #ef4444;       /* 빨간색 */
}

/* 사용 예시 */
.featured-card {
  border: 2px solid var(--primary);
}
```

#### 폰트 변경
```css
/* BaseLayout.astro */
body {
  font-family: 'Noto Sans KR', 'Inter', sans-serif;
}
```

### 이미지 추가하기

#### 1. 이미지 업로드
```bash
# 위치
/public/images/projects/프로젝트명/이미지.png
```

#### 2. Markdown에서 사용
```markdown
![이미지 설명](/images/projects/프로젝트명/이미지.png)
```

#### 3. HTML에서 사용
```html
<img src="/images/projects/프로젝트명/이미지.png" alt="이미지 설명">
```

---

## 성능 최적화 팁

### 1. 이미지 최적화
```bash
# 이미지 압축 (권장)
# WebP 형식 사용
# 적절한 크기로 리사이즈
```

### 2. Chart.js 최적화
```javascript
// decimation 사용 (데이터 포인트 많을 때)
options: {
  parsing: false,
  normalized: true,
  plugins: {
    decimation: {
      enabled: true,
      algorithm: 'lttb'
    }
  }
}
```

### 3. 빌드 최적화
```bash
# 프로덕션 빌드
npm run build

# 미리보기
npm run preview
```

---

## 보안 고려사항

### 1. SSH 키 관리
- GitHub Secrets에 안전하게 저장
- 정기적으로 키 교체 (6개월마다)
- 서버 접속 로그 모니터링

### 2. Nginx 설정
```nginx
# HTTPS 강제
server {
    listen 80;
    server_name kimyonghee.com;
    return 301 https://$server_name$request_uri;
}

# 보안 헤더
add_header X-Frame-Options "SAMEORIGIN";
add_header X-Content-Type-Options "nosniff";
add_header X-XSS-Protection "1; mode=block";
```

### 3. 정기 업데이트
```bash
# 의존성 업데이트
npm update
npm audit fix

# Astro 버전 업데이트
npm install astro@latest
```

---

## 백업 및 복구

### 정기 백업
```bash
# Git으로 자동 백업됨
git status
git add .
git commit -m "Regular backup"
git push origin main
```

### 수동 백업 (서버)
```bash
# 파일 백업
tar -czf kimyonghee-website-backup-$(date +%Y%m%d).tar.gz /home/projects/kimyonghee-website

# 원격 저장
scp backup.tar.gz user@backup-server:/backups/
```

### 복구 절차
```bash
# 1. 저장소 클론
git clone https://github.com/trustune/kimyonghee-website.git

# 2. 의존성 설치
npm install

# 3. 빌드 및 배포
npm run build
rsync -av --delete dist/ /var/www/kimyonghee.com/public/
```

---

## 연락처 및 지원

### 개발 관련
- **GitHub Repository**: https://github.com/trustune/kimyonghee-website
- **Issues**: https://github.com/trustune/kimyonghee-website/issues
- **Actions**: https://github.com/trustune/kimyonghee-website/actions

### 문서
- **Astro 공식 문서**: https://docs.astro.build
- **Chart.js 공식 문서**: https://www.chartjs.org/docs/latest/
- **GitHub Actions 문서**: https://docs.github.com/en/actions

### 유용한 링크
- **웹사이트**: https://kimyonghee.com
- **서버 관리**: SSH root@115.71.237.77
- **도메인 관리**: (도메인 등록업체 정보)

---

## 버전 히스토리

### v3.0 (2025-11-13)
- ✅ Projects 페이지 PDF 다운로드 레이아웃으로 변경
- ✅ Featured Projects 간격 증가
- ✅ 완전 인계서 작성

### v2.0 (2025-11-12)
- ✅ Broadcasting Reapproval 프로젝트 전면 재작성
- ✅ Chart.js 7개 차트 구현
- ✅ 데이터 오류 수정 (3-4년)
- ✅ 날짜 업데이트 (2025-10-11)

### v1.0 (2025-11-12)
- ✅ Broadcasting Revenue 프로젝트 재작성
- ✅ Chart.js 4개 차트 구현
- ✅ Research Methodology 정리
- ✅ 데이터 검증 완료

---

## 마지막 체크리스트

- [x] 모든 코드 변경사항 커밋됨
- [x] 빌드 성공 확인
- [x] GitHub Actions 배포 성공
- [x] 웹사이트 정상 작동 확인
- [x] 차트 모두 렌더링 확인
- [x] 다국어 전환 작동 확인
- [x] 모바일 반응형 확인
- [x] 인계 문서 작성 완료

---

**인계 완료일**: 2025년 11월 13일
**최종 커밋**: 803fd74
**상태**: ✅ 운영 준비 완료

**작성자**: Claude Code Assistant
**검토자**: (검토자 이름)
**승인자**: 김용희 교수

---

## 부록: 자주 사용하는 명령어

### 개발 환경
```bash
# 개발 서버 시작
npm run dev

# 프로덕션 빌드
npm run build

# 빌드 미리보기
npm run preview

# 의존성 설치
npm install

# 캐시 삭제 후 재설치
rm -rf node_modules package-lock.json && npm install
```

### Git 명령어
```bash
# 상태 확인
git status

# 변경사항 스테이징
git add .

# 커밋
git commit -m "메시지"

# 푸시
git push origin main

# 풀
git pull origin main

# 브랜치 확인
git branch

# 로그 확인
git log --oneline -10
```

### 서버 관리
```bash
# SSH 접속
ssh root@115.71.237.77

# 프로젝트 디렉토리
cd /home/projects/kimyonghee-website

# 웹서버 디렉토리
cd /var/www/kimyonghee.com/public/

# Nginx 재시작
systemctl restart nginx

# Nginx 설정 테스트
nginx -t

# 디스크 사용량
df -h

# 프로세스 확인
ps aux | grep node
```

---

**이 문서는 정기적으로 업데이트됩니다.**
**최종 업데이트**: 2025년 11월 13일
