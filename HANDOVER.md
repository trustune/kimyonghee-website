# 인계서 (Handover Document)

**최종 업데이트**: 2025년 11월 12일 21:30 KST  
**프로젝트**: kimyonghee.com 학술 웹사이트  

---

## 📋 목차

1. [프로젝트 개요](#프로젝트-개요)
2. [현재 상태](#현재-상태)
3. [완료된 작업 (2025-11-12 세션)](#완료된-작업-2025-11-12-세션)
4. [차트 구현 가이드 (중요!)](#차트-구현-가이드-중요)
5. [표 스타일 가이드](#표-스타일-가이드)
6. [공유 버튼 구현](#공유-버튼-구현)
7. [기술 스택 및 구조](#기술-스택-및-구조)
8. [배포 프로세스](#배포-프로세스)
9. [문제 해결 가이드](#문제-해결-가이드)
10. [주요 파일 위치](#주요-파일-위치)

---

## 프로젝트 개요

### 목표
- 경영학과 교수(김용희)의 전문 학술 웹사이트 구축
- 연구 성과물, 강의 자료, 프로젝트, 블로그 통합 관리
- Nathan Lane (https://nathanlane.info/) 수준의 전문성

### 핵심 원칙
1. **데이터 진실성**: 실제 데이터만 사용, 가짜 데이터 절대 금지
2. **학술적 신뢰성**: 출처 명확, 데이터 검증 강조
3. **전문성**: 고품질 디자인과 콘텐츠
4. **자동화**: GitHub Actions를 통한 자동 배포

---

## 현재 상태

### ✅ 완료된 기능
1. **홈페이지**: 프로필, 최신 연구, 블로그 피드
2. **Research 섹션**: 13개 논문 (진행중/출판됨/발표됨)
3. **Projects 섹션**: 
   - 방송산업 순유입재원 분석 (2015-2024)
   - 인터랙티브 Chart.js 그래프 3개
   - 상세 데이터 표 및 분석
   - 소셜 공유 버튼
4. **Blog**: 3개 포스트
5. **Teaching**: 4개 강의
6. **CV**: 자동 생성 시스템
7. **Media**: 미디어 기고 6건
8. **About**: 프로필 페이지
9. **Search**: Pagefind 검색 기능

### 🌐 배포 상태
- **도메인**: https://kimyonghee.com
- **서버**: Ubuntu 20.04 LTS (115.71.237.77:2222)
- **웹서버**: Nginx
- **자동 배포**: GitHub Actions (정상 작동)

---

## 완료된 작업 (2025-11-12 세션)

### 1. Chart.js 렌더링 문제 수정
**문제**: 차트가 렌더링되지 않음 ("can't acquire context from the given item")

**해결**:
- `<div>` → `<canvas>` 요소로 변경
- 초기화 로직 개선 (IIFE, 에러 핸들링)
- Canvas 크기 검증 및 재시도 로직 추가

### 2. 차트 위치 조정
**문제**: 차트가 페이지 맨 끝에 표시됨

**해결**:
- MDX를 Markdown으로 변경 (빌드 에러 해결)
- HTML 주석 마커 사용: `<!-- CHART:chartId -->`
- JavaScript로 주석을 실제 차트로 교체

### 3. 표 폰트 통일
**변경 전**: Inter (헤더/셀) + Monaco (숫자)  
**변경 후**: Paperozi 폰트로 전체 통일 + tabular-nums

### 4. 페이지 레이아웃 개선
- 프로젝트 상세 페이지 max-width: 800px → 1100px
- 차트와 표가 더 넓게 표시됨

### 5. Favicon 추가
- `/public/favicon.svg` 생성 (파란색 배경, 흰색 "Y")
- BaseLayout에 favicon 링크 추가

### 6. 소셜 공유 버튼 추가
- 프로젝트 페이지에 Twitter, Facebook, LinkedIn, Bluesky 공유 버튼 추가
- SocialShare 컴포넌트 재사용

---

## 차트 구현 가이드 (중요!)

### ⚠️ 주의사항

#### 1. **반드시 Markdown 파일 사용 (.md)**
```
✅ 올바름: broadcasting-revenue-2015-2024.md
❌ 잘못됨: broadcasting-revenue-2015-2024.mdx
```

**이유**: 
- MDX는 `<style>` 블록과 JSX 구문 충돌로 빌드 에러 발생
- Markdown은 HTML을 직접 지원하므로 문제 없음

#### 2. **HTML 주석으로 차트 마커 표시**
```markdown
### Section Title

설명 텍스트...

<!-- CHART:chartId -->

이어지는 내용...
```

**규칙**:
- `<!-- CHART:` + `차트ID` + ` -->`
- 정확한 공백과 대소문자 필수
- 차트를 원하는 위치에 정확히 배치

#### 3. **[slug].astro에 차트 데이터 정의**

```astro
---
// Chart data 정의
const revenueLabels = ['2015', '2016', ...];
const revenueDatasets = [
  {
    label: 'Pay-TV Subscriptions',
    data: [27.5, 28.3, 29.4, ...],
    borderColor: 'rgba(102, 126, 234, 1)',
    backgroundColor: 'rgba(102, 126, 234, 0.1)',
    borderWidth: 3,
    fill: true,
    tension: 0.4
  }
];
---
```

#### 4. **차트 컨테이너 생성**

```astro
{showCharts && (
  <>
    <div id="chart-container-revenue" style="display: none;">
      <LineChart
        chartId="revenueChart"
        title="Net Inflow Revenue Trends (2015-2024)"
        labels={revenueLabels}
        datasets={revenueDatasets}
        yAxisLabel="Amount (Trillion Won)"
        yAxisCallback={true}
      />
    </div>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        const projectContent = document.querySelector('.project-content');
        const walker = document.createTreeWalker(
          projectContent,
          NodeFilter.SHOW_COMMENT,
          null
        );

        const comments = [];
        let node;
        while (node = walker.nextNode()) {
          comments.push(node);
        }

        comments.forEach(comment => {
          const text = comment.textContent.trim();
          if (text === 'CHART:revenueChart') {
            const container = document.getElementById('chart-container-revenue');
            if (container) {
              container.style.display = 'block';
              comment.parentNode.replaceChild(container, comment);
            }
          }
        });
      });
    </script>
  </>
)}
```

### 차트 추가 단계별 가이드

#### Step 1: Markdown에 마커 추가
```markdown
<!-- CHART:myNewChart -->
```

#### Step 2: [slug].astro에 데이터 정의
```astro
const myNewLabels = ['2020', '2021', '2022'];
const myNewDatasets = [{
  label: 'Dataset Name',
  data: [10, 20, 30],
  borderColor: 'rgba(255, 99, 132, 1)',
  backgroundColor: 'rgba(255, 99, 132, 0.1)',
  borderWidth: 3,
  fill: true,
  tension: 0.4
}];
```

#### Step 3: 차트 컨테이너 추가
```astro
<div id="chart-container-mynew" style="display: none;">
  <LineChart
    chartId="myNewChart"
    title="My New Chart Title"
    labels={myNewLabels}
    datasets={myNewDatasets}
    yAxisLabel="Y Axis Label"
    yAxisCallback={false}
  />
</div>
```

#### Step 4: JavaScript에 처리 로직 추가
```javascript
if (text === 'CHART:myNewChart') {
  const container = document.getElementById('chart-container-mynew');
  if (container) {
    container.style.display = 'block';
    comment.parentNode.replaceChild(container, comment);
  }
}
```

#### Step 5: 빌드 테스트
```bash
npm run build
```

### Chart.js 색상 팔레트

**추천 색상 조합**:
```javascript
// 파란색 계열
borderColor: 'rgba(102, 126, 234, 1)'
backgroundColor: 'rgba(102, 126, 234, 0.1)'

// 빨간색 계열
borderColor: 'rgba(239, 68, 68, 1)'
backgroundColor: 'rgba(239, 68, 68, 0.1)'

// 주황색 계열
borderColor: 'rgba(245, 158, 11, 1)'
backgroundColor: 'rgba(245, 158, 11, 0.1)'

// 초록색 계열
borderColor: 'rgba(16, 185, 129, 1)'
backgroundColor: 'rgba(16, 185, 129, 0.1)'

// 파란색 계열 (밝음)
borderColor: 'rgba(59, 130, 246, 1)'
backgroundColor: 'rgba(59, 130, 246, 0.1)'
```

### 차트 옵션

**yAxisCallback**:
- `true`: Y축에 "T" 접미사 추가 (예: "10T")
- `false`: 숫자만 표시 (예: "10")

**borderDash**:
- `[5, 5]`: 점선 (5px 선, 5px 공백)
- 생략 시 실선

**tension**:
- `0.4`: 부드러운 곡선
- `0`: 직선

---

## 표 스타일 가이드

### 기본 스타일

프로젝트 Markdown 파일의 `<style>` 블록에 포함:

```css
.data-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin: 2rem 0;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.data-table thead {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.data-table th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  font-size: 1rem;
  font-family: 'Paperozi', 'Inter', sans-serif;
}

.data-table td {
  padding: 1rem;
  font-size: 1rem;
  color: #374151;
  font-family: 'Paperozi', 'Inter', sans-serif;
}

.data-table .number {
  text-align: right;
  font-family: 'Paperozi', 'Inter', sans-serif;
  font-weight: 500;
  font-variant-numeric: tabular-nums; /* 숫자 정렬 개선 */
}

.data-table .positive {
  color: #059669;
  font-weight: 600;
}

.data-table .negative {
  color: #dc2626;
  font-weight: 600;
}
```

### 표 사용 예시

```html
<table class="data-table">
<thead>
<tr>
<th>Year</th>
<th class="number">Amount</th>
<th class="number">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td>2024</td>
<td class="number">8.89T won</td>
<td class="number positive">+25.90%</td>
</tr>
<tr>
<td>2015</td>
<td class="number">7.06T won</td>
<td class="number negative">-10.00%</td>
</tr>
</tbody>
</table>
```

### 폰트 설정

**중요**: 모든 텍스트에 Paperozi 폰트 사용
```css
font-family: 'Paperozi', 'Inter', sans-serif;
```

**숫자 정렬**:
```css
font-variant-numeric: tabular-nums;
```
→ 숫자를 고정 너비로 표시하여 세로 정렬 개선

---

## 공유 버튼 구현

### SocialShare 컴포넌트

**위치**: `/src/components/SocialShare.astro`

**사용법**:
```astro
import SocialShare from '../../components/SocialShare.astro';

<SocialShare
  title={data.title_en}
  url={`https://kimyonghee.com/projects/${project.slug}`}
  excerpt={data.summary}
/>
```

**Props**:
- `title`: 공유할 제목
- `url`: 공유할 URL (전체 경로)
- `excerpt`: 요약 (선택사항)

**지원 플랫폼**:
1. Twitter: 제목 + 요약 + URL
2. Facebook: URL만
3. LinkedIn: 제목 + URL + 요약
4. Bluesky: 제목 + 요약 + URL

---

## 기술 스택 및 구조

### 프론트엔드
- **프레임워크**: Astro 4.x
- **스타일링**: 커스텀 CSS (Tailwind 미사용)
- **타이포그래피**: 
  - 본문: Paperozi (한글), Merriweather (영문)
  - UI: Inter
- **아이콘**: Lucide React
- **차트**: Chart.js 4.4.0 (ESM from CDN)
- **검색**: Pagefind

### 백엔드/배포
- **서버**: Ubuntu 20.04 LTS
- **웹서버**: Nginx
- **Node.js**: v20.x
- **빌드**: Astro static site generation
- **CI/CD**: GitHub Actions

### 주요 디렉토리 구조

```
/home/projects/kimyonghee-website/
├── src/
│   ├── pages/              # 페이지 라우팅
│   │   ├── index.astro
│   │   ├── projects/
│   │   │   ├── index.astro
│   │   │   └── [slug].astro
│   │   ├── research/
│   │   ├── blog/
│   │   └── teaching.astro
│   ├── content/            # 마크다운 콘텐츠
│   │   ├── blog/
│   │   └── projects/
│   │       └── broadcasting-revenue-2015-2024.md
│   ├── data/               # JSON 데이터
│   │   ├── publications.json
│   │   ├── courses/
│   │   └── cv.json
│   ├── layouts/
│   │   └── BaseLayout.astro
│   └── components/
│       ├── LineChart.astro
│       └── SocialShare.astro
├── public/
│   ├── favicon.svg
│   └── images/
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## 배포 프로세스

### 자동 배포 (권장)

```powershell
# 로컬에서 작업
cd D:\PROJECT_2025\kimyonghee-website

# 변경사항 커밋
git add .
git commit -m "설명"
git push origin main
```

**자동 배포 흐름**:
1. GitHub Actions 실행
2. 서버 SSH 접속
3. git pull
4. npm install
5. npm run build
6. rsync로 `/var/www/kimyonghee.com/public/` 배포

**소요 시간**: 약 1-2분

### 수동 배포 (백업)

```bash
# 서버 접속
ssh -p 2222 root@kimyonghee.com

# 배포
cd /home/projects/kimyonghee-website
git pull origin main
npm install
npm run build
rsync -avz --delete dist/ /var/www/kimyonghee.com/public/
```

### 로컬 빌드 테스트

```bash
# 빌드
npm run build

# 미리보기
npm run preview
```

**빌드 성공 확인**:
```
✓ Completed in XXs
[build] 33 page(s) built
[build] Complete!
Pagefind indexed XX pages
```

---

## 문제 해결 가이드

### 1. 빌드 에러: MDX 파싱 오류

**에러 메시지**:
```
[@mdx-js/rollup] Could not parse expression with acorn
```

**원인**: MDX 파일의 `<style>` 블록과 JSX 구문 충돌

**해결**:
```bash
# MDX를 MD로 변경
mv file.mdx file.md

# 차트 마커를 HTML 주석으로 변경
<!-- CHART:chartId -->
```

### 2. 차트가 렌더링되지 않음

**확인사항**:
1. Canvas 요소 사용 (`<canvas>` not `<div>`)
2. Chart.js CDN 로드 확인
3. 차트 ID가 중복되지 않는지 확인
4. 브라우저 콘솔에서 에러 확인

**디버깅**:
```javascript
// 브라우저 콘솔
console.log(document.getElementById('chartId'));
console.log(document.getElementById('chartId')._chartInstance);
```

### 3. 차트가 페이지 맨 끝에 표시

**원인**: JavaScript가 주석 마커를 찾지 못함

**확인**:
1. 주석 형식 정확한지: `<!-- CHART:chartId -->`
2. JavaScript의 차트 ID가 일치하는지
3. `TreeWalker`가 정상 작동하는지

### 4. 페이지가 업데이트되지 않음

**해결**:
```
Ctrl + Shift + Delete → 전체 기간 캐시 삭제
Ctrl + Shift + R (강제 새로고침)
시크릿 모드로 확인
```

### 5. Favicon이 표시되지 않음

**확인**:
1. `/public/favicon.svg` 존재 확인
2. `BaseLayout.astro`에 링크 있는지 확인
3. 브라우저 캐시 삭제

### 6. 표 폰트가 적용되지 않음

**확인**:
1. `<style>` 블록이 Markdown 파일에 있는지
2. CSS 선택자가 정확한지 (`.data-table`)
3. 폰트 이름: `'Paperozi'` (대소문자 정확히)

---

## 주요 파일 위치

### 차트 관련
- **LineChart 컴포넌트**: `src/components/LineChart.astro`
- **프로젝트 레이아웃**: `src/pages/projects/[slug].astro`
- **프로젝트 콘텐츠**: `src/content/projects/broadcasting-revenue-2015-2024.md`

### 스타일 관련
- **기본 레이아웃**: `src/layouts/BaseLayout.astro`
- **Paperozi 폰트 로드**: `BaseLayout.astro` (CDN)

### 데이터 파일
- **Publications**: `src/data/publications.json`
- **Courses**: `src/data/courses/*.json`
- **CV**: `src/data/cv.json`

### 배포 관련
- **GitHub Actions**: `.github/workflows/deploy.yml`
- **Nginx 설정**: `/etc/nginx/sites-available/` (서버)

---

## 추가 개선 제안

### 즉시 가능
1. 프로젝트 추가 (현재 1개만 있음)
2. 블로그 포스트 정기 업데이트
3. 논문 상태 업데이트 (In Progress → Published)

### 중장기
1. 다국어 지원 (i18n)
2. D3.js로 복잡한 시각화
3. 검색 기능 고도화 (필터, 패싯)
4. 성능 최적화 (이미지 WebP, lazy loading)
5. Google Analytics 또는 Plausible 추가

---

## 중요 참고사항

### 데이터 진실성 (절대 규칙)
- ❌ 가짜 데이터 생성 금지
- ❌ 임의 데이터 생성 금지
- ❌ 예시 데이터를 실제처럼 표시 금지
- ✅ 없는 데이터는 "Coming Soon" 또는 비워두기
- ✅ 모든 데이터 출처 명확히

### Git 커밋 메시지 컨벤션
```
[Type]: [간단한 설명]

예시:
feat: Add new chart to broadcasting project
fix: Resolve chart rendering issue
style: Update table fonts to Paperozi
docs: Update handover document
refactor: Simplify chart injection logic
```

### 코딩 스타일
- **간결함**: 불필요한 주석 최소화
- **실용성**: 작동하는 코드 우선
- **가독성**: 명확한 변수명
- **일관성**: 기존 코드 스타일 유지

---

## 연락처 및 리소스

### GitHub Repository
- **URL**: https://github.com/trustune/kimyonghee-website
- **Access**: GitHub 계정으로 접근 (Token은 별도 관리)

### 서버 정보
- **Domain**: https://kimyonghee.com
- **IP**: 115.71.237.77
- **Port**: 2222
- **User**: root

### 유용한 문서
- **Astro**: https://docs.astro.build
- **Chart.js**: https://www.chartjs.org/docs/
- **Pagefind**: https://pagefind.app/
- **참고 사이트**: https://nathanlane.info/

---

## 버전 히스토리

### v8.0 (2025-11-12 21:30)
- ✅ Chart.js 렌더링 문제 해결
- ✅ 차트를 콘텐츠 내 적절한 위치에 배치
- ✅ 표 폰트를 Paperozi로 통일
- ✅ 프로젝트 페이지 레이아웃 확대 (1100px)
- ✅ Favicon 추가
- ✅ 프로젝트 페이지에 공유 버튼 추가
- ✅ MDX 빌드 에러 해결 (MD로 변경)
- ✅ 인계서 작성

### v7.0 (이전)
- Projects 페이지 완전 영문화
- 방송산업 프로젝트 콘텐츠 대폭 확장
- Chart.js 그래프 3개 추가
- 스타일링 개선

---

## 마무리 체크리스트

다음 세션 시작 전 확인:

- [ ] 웹사이트 정상 작동 (https://kimyonghee.com)
- [ ] GitHub Actions 최근 실행 성공
- [ ] 로컬 저장소 최신 상태 (`git pull`)
- [ ] 이 인계서 읽기
- [ ] 새로운 작업 목표 정의

---

**일시**: 2025년 11월 12일 21:30 KST  
**다음 업데이트**: 다음 작업 세션 후
