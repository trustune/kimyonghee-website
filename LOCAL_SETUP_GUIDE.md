# 로컬 PC 개발 환경 설정 가이드

이 가이드를 따라하면 로컬 PC에서 코드를 수정하고 GitHub에 push하면 자동으로 서버에 배포됩니다.

## 🎯 목표

```
로컬 PC 수정 → Git commit → Git push → GitHub Actions 자동 실행 → 서버 자동 배포
```

---

## 📋 사전 준비사항

### 1. 소프트웨어 설치 (Windows)

**Git 설치:**
- https://git-scm.com/download/win 다운로드
- 설치 시 기본 옵션으로 진행
- 설치 후 확인:
  ```bash
  git --version
  ```

**Node.js 설치:**
- https://nodejs.org/ (LTS 버전 권장: 20.x)
- 다운로드 후 설치
- 설치 후 확인:
  ```bash
  node --version
  npm --version
  ```

**VS Code 설치 (권장):**
- https://code.visualstudio.com/
- 코드 편집기 (선택사항이지만 강력 추천)

---

## 🚀 1단계: GitHub 설정

### A. GitHub Actions Secrets 설정

1. **GitHub 저장소로 이동:**
   - https://github.com/trustune/kimyonghee-website

2. **Settings → Secrets and variables → Actions 클릭**

3. **다음 3개의 Secret 추가 (New repository secret):**

   **① HOST**
   ```
   Name: HOST
   Value: 115.71.237.77
   ```

   **② USERNAME**
   ```
   Name: USERNAME
   Value: root
   ```

   **③ SSH_KEY**
   ```
   Name: SSH_KEY
   Value: (아래 SSH 키 복사)
   ```

   SSH 키 내용:
   ```
   -----BEGIN OPENSSH PRIVATE KEY-----
   b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
   QyNTUxOQAAACBNq3fhPebC3FOUu0PRlu/EbEy7VV780Va2uFm1GlfdKAAAAJg2TtvjNk7b
   4wAAAAtzc2gtZWQyNTUxOQAAACBNq3fhPebC3FOUu0PRlu/EbEy7VV780Va2uFm1GlfdKA
   AAAECSehXX2YGkWUBwEkkkHUhoRZe52fCh8uGJJoqvSTeKCE2rd+E95sLcU5S7Q9GW78Rs
   TLtVXvzRVra4WbUaV90oAAAAFWdpdGh1Yi1hY3Rpb25zLWRlcGxveQ==
   -----END OPENSSH PRIVATE KEY-----
   ```

4. **저장 확인**
   - 3개의 Secret이 모두 추가되었는지 확인

---

## 💻 2단계: 로컬 PC에 프로젝트 클론

### Windows PowerShell 또는 Git Bash에서 실행:

```bash
# 1. 프로젝트를 저장할 폴더로 이동
cd C:\Users\YourName\Projects
# (폴더 경로는 원하는 대로 변경 가능)

# 2. GitHub에서 프로젝트 클론
git clone https://github.com/trustune/kimyonghee-website.git

# 3. 프로젝트 폴더로 이동
cd kimyonghee-website

# 4. 의존성 설치
npm install

# 5. 개발 서버 실행 (테스트)
npm run dev
```

브라우저에서 `http://localhost:4321` 접속하여 확인

---

## ✏️ 3단계: 작업 흐름 (일상적인 사용법)

### A. 코드 수정하기

1. **VS Code에서 프로젝트 열기:**
   ```bash
   code .
   ```

2. **파일 수정:**
   - 예: `src/pages/index.astro` 수정
   - 예: `public/projects/broadcasting/detailed_analysis.json` 데이터 수정

3. **로컬에서 테스트:**
   ```bash
   npm run dev
   ```
   - 브라우저에서 확인 (http://localhost:4321)

### B. GitHub에 푸시하기 (자동 배포)

```bash
# 1. 변경사항 확인
git status

# 2. 변경된 파일 스테이징
git add .

# 3. 커밋 (메시지는 작업 내용에 맞게 변경)
git commit -m "Update broadcasting analysis data"

# 4. GitHub에 푸시 (자동 배포 시작!)
git push origin main
```

### C. 배포 확인

1. **GitHub Actions 확인:**
   - https://github.com/trustune/kimyonghee-website/actions
   - 자동으로 워크플로우 실행됨
   - 약 2-3분 소요

2. **웹사이트 확인:**
   - https://kimyonghee.com 접속
   - 변경사항 반영 확인

---

## 📁 주요 파일 위치

### 자주 수정하는 파일들:

```
kimyonghee-website/
├── src/
│   ├── pages/                    # 페이지 파일들
│   │   ├── index.astro          # 홈페이지
│   │   ├── about.astro          # 소개
│   │   ├── blog/
│   │   │   └── [slug].astro     # 블로그 포스트
│   │   └── projects/
│   │       └── [slug].astro     # 프로젝트 상세
│   ├── components/              # 재사용 가능한 컴포넌트
│   └── data/                    # 데이터 파일
│       ├── publications.json    # 논문 데이터
│       ├── blog.json            # 블로그 데이터
│       └── media.json           # 미디어 데이터
├── public/                      # 정적 파일
│   ├── images/                  # 이미지
│   └── projects/                # 프로젝트 데이터
│       └── broadcasting/
│           ├── net_inflow_summary.json
│           └── detailed_analysis.json
└── .github/workflows/
    └── deploy.yml               # 자동 배포 설정
```

---

## 🔧 유용한 명령어

```bash
# 개발 서버 실행
npm run dev

# 프로덕션 빌드 (로컬 테스트)
npm run build

# 빌드 결과 미리보기
npm run preview

# 최신 코드 가져오기 (서버에서 다른 곳에서 수정한 경우)
git pull origin main

# Git 상태 확인
git status

# 변경사항 되돌리기 (커밋 전)
git restore 파일명

# 브랜치 확인
git branch
```

---

## 🐛 문제 해결

### 문제 1: `git push` 시 인증 오류

**해결방법:**
1. GitHub Personal Access Token 생성:
   - GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Generate new token
   - 권한: `repo` 전체 선택
   - 토큰 복사

2. Git credential 설정:
   ```bash
   git config credential.helper store
   git push origin main
   ```
   - Username: trustune
   - Password: (생성한 Token 붙여넣기)

### 문제 2: GitHub Actions 실패

1. **Actions 탭에서 에러 로그 확인:**
   - https://github.com/trustune/kimyonghee-website/actions
   - 실패한 워크플로우 클릭
   - 에러 메시지 확인

2. **자주 발생하는 문제:**
   - Secrets 설정 누락 → 다시 확인
   - 서버 SSH 접속 실패 → 서버 상태 확인
   - 빌드 에러 → 로컬에서 `npm run build` 테스트

### 문제 3: `npm install` 실패

```bash
# npm 캐시 삭제 후 재시도
npm cache clean --force
npm install
```

### 문제 4: 포트 충돌 (4321 이미 사용 중)

```bash
# 다른 포트로 실행
npm run dev -- --port 3000
```

---

## 📊 자동 배포 프로세스

```
1. 로컬에서 코드 수정
   ↓
2. git commit & push
   ↓
3. GitHub이 push 감지
   ↓
4. GitHub Actions 실행:
   - Node.js 20 설치
   - npm install
   - npm run build (테스트)
   ↓
5. 서버에 SSH 접속:
   - git pull origin main
   - npm install
   - npm run build
   - rsync로 웹서버 폴더에 복사
   ↓
6. 배포 완료! ✅
```

---

## 💡 팁 & 모범 사례

### 커밋 메시지 작성법

```bash
# 좋은 예:
git commit -m "Add new publication about media economics"
git commit -m "Update broadcasting revenue data for 2024"
git commit -m "Fix navigation menu on mobile"

# 나쁜 예:
git commit -m "update"
git commit -m "fix"
```

### 자주 푸시하기

- 작은 단위로 자주 커밋하고 푸시
- 큰 변경사항은 여러 개의 작은 커밋으로 분리

### 테스트 후 푸시

```bash
# 항상 로컬에서 테스트 후 푸시
npm run dev    # 개발 서버에서 확인
npm run build  # 빌드 에러 없는지 확인
git push       # 문제 없으면 푸시
```

---

## 📞 추가 도움

- **GitHub 저장소:** https://github.com/trustune/kimyonghee-website
- **GitHub Actions 로그:** https://github.com/trustune/kimyonghee-website/actions
- **웹사이트:** https://kimyonghee.com

---

**마지막 업데이트:** 2025-11-12
**작성자:** Claude Code Assistant
