casual infrerence in panel data 
# 📘 Research Lab System v7.0 : THE MANIFESTO & SPECIFICATION

## 0. Project Manifesto (기획 의도 및 철학)

**"우리는 더 이상 검색(Search)하지 않는다. 연구(Research)한다."**

이 프로젝트의 목적은 단순한 논문 요약 봇을 만드는 것이 아닙니다. **128GB RAM과 4070 Super**라는 강력한 로컬 자원을 기반으로, **인간 연구자(교수)의 인지 능력을 확장하는 '디지털 연구 동반자(Digital Research Partner)'**를 구축하는 것입니다.

기존 상용 서비스(Liner, SciSpace)의 한계인 **'텍스트 중심의 얕은 분석'**과 **'데이터 보안 우려'**를 타파하고, **'시각(Vision) 기반의 심층 분석'**, **'통계적 엄밀성(R-Stat)'**, **'연구 윤리 준수(Verification)'**를 달성하는 것이 핵심 목표입니다.

---

## 1. 🏗️ Infrastructure: "Local Powerhouse"

[Context & Purpose]

클라우드 지연 시간(Latency)을 없애고, 모든 데이터 처리를 **Memory-Speed(램 속도)**로 처리하여 "생각의 속도"로 연구할 수 있는 환경을 만든다.

**[Specification]**

- **Docker Compose:** 다음 4개의 컨테이너를 유기적으로 연결.
    
    1. **Qdrant (The Memory):**
        
        - _Purpose:_ 디스크 I/O 병목 제거. 10만 건의 논문도 0.01초 안에 검색.
            
        - _Config:_ `memmap_threshold_kb: 1000000` (128GB RAM 활용, Disk Offload 금지).
            
    2. **Neo4j (The Context):**
        
        - _Purpose:_ 논문 간의 인용 관계(Citation Network)를 그래프로 시각화하여 "연구의 맥락" 파악.
            
        - _Config:_ Heap Size 16GB 할당.
            
    3. **R-Server (The Analyst):**
        
        - _Purpose:_ LLM이 흉내만 내는 통계가 아니라, **실제 학술 논문에 쓸 수 있는 검증된 통계(APA Style)** 산출.
            
        - _Image:_ `rocker/verse:latest` (JASP/Jamovi를 대체할 엔진).
            
    4. **Redis (The Accelerator):**
        
        - _Purpose:_ 외부 API(Google, S2) 호출 비용 절감 및 속도 향상.
            

---

## 2. 🔐 Security & Data: "Your Data, Your Rules"

[Context & Purpose]

연구 데이터는 교수의 지적 재산이다. 판매용 서비스가 아니므로 복잡한 회원가입은 배제하되, 다중 사용자(동료 교수/학생)가 각자의 API 키(BYOK)를 안전하게 쓰며 연구 데이터를 완벽히 격리해야 한다.

**[Specification]**

- **BYOK (Bring Your Own Key):**
    
    - `.env`에 키를 일단 두고 추후 공개된 서버로 마이그래이션하면 키를 두지 않는다. DB에 사용자별로 키를 암호화(AES-256)하여 저장한다.
        
    - 목적: 비용 투명성 확보 및 보안 강화.
        
- **Project Isolation (Silo Effect):**
    
    - _Logic:_ A 프로젝트의 RAG 검색 결과에 B 프로젝트의 논문이 절대 섞이면 안 됨.
        
    - _Implementation:_ 모든 DB 쿼리에 `project_id` 필터를 **강제 주입(Hard Enforcement)**.
        

---

## 3. 👁️ Vision RAG: "See as Humans See"

[Context & Purpose]

논문의 핵심은 텍스트가 아니라 **표(Table)**와 **그래프(Chart)**에 있다. 기존의 텍스트 추출(OCR) 방식은 표를 깨뜨려 연구 가치를 훼손한다. 우리는 "문서를 이미지로 보고 이해하는" 차세대 방식을 채택한다.

**[Specification]**

- **Engine:** `Gemini 2.5 Flash` (Vision API).
    
- **Process:** PDF → High-Res Image → Gemini Vision Analysis → Markdown.
    
- **Critical Instruction:**
    
    - *"단순히 글자를 읽지 마라. 이미지 내의 **표 구조(Row/Column)*_를 완벽한 Markdown Table로 복원하고, **그래프의 추세(Trend)와 수치**를 해석하여 텍스트로 서술하라."_
        

---

## 4. 📈 Statistical Engine: "Beyond JASP"

[Context & Purpose]

클릭만 편한 JASP/Jamovi를 넘어, "복잡한 계량경제(PVAR, GMM)까지 가능하면서도, 결과표는 논문에 바로 붙여넣을 수 있는(Publication-Ready)" 자동화된 분석 시스템이 필요하다.

**[Specification]**

- **Core:** `src/services/r_bridge.py`.
    
- **Agent (GPT-5):** 사용자 말("이 변수들로 구조방정식 돌려줘")을 R 코드(`lavaan`)로 변환.
- 임의로 코딩하기 보다는 라이브러리에 있는 표준화된 방법을 사용하도록 권고. 옵션같은것도 파악해서 알려주고 최대한 많은 결과를 도출
    
- **Reporting:**
    
    - 반드시 **`stargazer`** (HTML) 또는 **`gtsummary`** 패키지 사용.
        
    - 결과물: _"t(24)=2.5, p<.01"_ 형태의 표준 학술 양식 자동 생성.
    
        
- **Advanced Modules:** `panelvar` (패널 시계열), `CausalImpact` (인과추론), `easystats` (자동 가정 검증).
    

---

## 5. 🤖 Specialized Agents: "The AI Research Team"

[Context & Purpose]

혼자 연구하지 않는다. AI를 각기 다른 전문성을 가진 동료로 정의하고 협업한다.

**[Specification]**

1. **🏛️ Review Committee (심사위원회):**
    
    - _Scout (Gemini):_ "이 논문이 저널 스코프에 맞나?" (Web Search).
        
    - _Critic (GPT-5):_ "통계적 방법론에 허점은 없나?" (Logic Check).
        
    - _Editor (Claude 4):_ "종합 판정(Accept/Reject) 및 리뷰 레터 작성."
        
2. **📚 Library Agent (성실한 조교):**
    
    - _Engine:_ Claude 4 Computer Use.
        
    - _Task:_ 도서관 로그인 및 PDF 다운로드.
        
    - _Safety:_ **"사람처럼 천천히(30~60초 딜레이)"** 행동하여 계정 차단을 막는다.
        
3. **⚖️ Citation Judge (깐깐한 판사):**
    
    - _Role:_ 사용자가 쓴 문장에 대해 추천 논문이 **진짜 근거가 되는지** 검증.
        

---

## 6. 🎨 UI/UX & Menu Structure (Streamlit)

[Context & Purpose]

복잡한 설정은 숨기고, **연구의 흐름(Workflow)**에 따라 자연스럽게 메뉴가 이어지도록 설계한다. 화면은 항상 **"자료(좌) - 분석(우)"**의 Split View를 유지하여 직관성을 높인다.

**[Menu Structure Detail]**

- **🏠 Dashboard (Home)**
    
    - 프로젝트 선택/생성, 최근 활동 로그, 시스템 상태(CPU/GPU) 모니터링.
        
- **1. 🔎 Search & Collect (자료 수집)**
    
    - _Feature:_ 논문 통합 검색(S2, Google), 리스트 검증(Validator), **[원클릭 RAG 저장]**.
        
- **2. 📚 My Library (서재)**
    
    - _Feature:_ 수집된 PDF 목록(Card View). Gemini Vision이 요약한 "표/그래프 미리보기".
        
- **3. 💬 RAG Chat (심층 분석)**
    
    - _Feature:_ 내 서재의 논문들과 대화. **Split View (좌: PDF 원문 하이라이트 / 우: AI 답변)**.
        
- **4. 📊 Statistics (통계 분석실)**
    
    - _Feature:_ CSV 업로드 -> Drag & Drop 변수 지정 -> **"JASP 스타일"** 분석 수행 -> APA 결과표 및 해석 출력.
        
- **5. 📝 Writer & Review (집필 및 심사)**
    
    - _Feature:_ 논문 초안 작성 지원(Citation Judge) 및 모의 Peer Review(Committee).
        
- **6. 🕸️ Research Tracer (지식 지도)**
    
    - _Feature:_ 내 논문들의 인용 관계를 Neo4j 그래프로 시각화.
        
- **7. ⚙️ Settings (설정)**
    
    - _Feature:_ **BYOK (API 키 입력)**, R-Server 상태 점검, 사용자 관리.
        

---

## 7. 🛣️ Execution Roadmap (구축 순서)

[Instruction]

AI 코더는 다음 단계를 엄수하여, 각 단계가 완벽히 검증된 후 다음으로 넘어가야 한다.

1. **Phase 0 (Clean Slate):** 기존 레거시 코드 전량 폐기 및 폴더 초기화.
    
2. **Phase 1 (Foundation):** `docker-compose.yml` (4개 컨테이너) 구동 및 DB 스키마(`models.py`) 확정.
    
3. **Phase 2 (The Eyes):** `Vision RAG Pipeline` (Ingest -> Gemini Vision -> Markdown -> Qdrant) 구현.
    
4. **Phase 3 (The Hands):** `R-Bridge` 연결 및 `Stat Agent` (GPT-5 + Stargazer) 구현.
    
5. **Phase 4 (The Team):** `Review Committee`, `Library Agent` 등 에이전트 로직 구현.
    
6. **Phase 5 (The Face):** Streamlit UI (Split View) 및 BYOK 설정 페이지 구현.
    

---

## 8. 🗂️ Project Directory Structure

**[Instruction]** 이 구조를 **되도록** 준수**하라.

Markdown

```
research_lab_v7/
├── .gitignore
├── docker-compose.yml           # Infra (Qdrant, Neo4j, Redis, R-Server)
├── requirements.txt             # Python Deps
├── requirements_r.txt           # R Packages (lavaan, panelvar, stargazer...)
├── data/                        # Volume Mounts
│   ├── qdrant/, neo4j/, analysis/
├── src/
│   ├── main.py
│   ├── database/
│   │   ├── models.py            # User, Project, Chat, Doc Tables
│   ├── rag/
│   │   ├── ingest.py            # Vision Processing (Gemini)
│   │   ├── chunker.py           # Header-based Semantic Chunking
│   ├── services/
│   │   ├── r_bridge.py          # Python-R Communication
│   │   ├── search_manager.py    # API Aggregator & Validator
│   │   ├── security.py          # Encryption Logic
│   └── agents/
│       ├── stat_agent.py        # Econometrics Logic
│       ├── review_committee.py  # Peer Review Logic
│       ├── library_agent.py     # Computer Use Logic
└── ui/
    ├── app.py                   # Main Entry
    └── pages/
        ├── 1_Search.py
        ├── 2_Library.py
        ├── 3_RAG_Chat.py
        ├── 4_Statistics.py
        ├── 5_Writer_Review.py
        ├── 6_Tracer.py
        └── 9_Settings.py
```
