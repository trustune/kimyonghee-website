"""
MediaINT Newsletter Manager
구독자 관리 + 주간 뉴스레터 발송 CLI

사용법:
  python manage.py sub list                     # 구독자 목록
  python manage.py sub add user@email.com       # 구독자 추가
  python manage.py sub add user@email.com "홍길동"  # 이름 포함 추가
  python manage.py sub remove user@email.com    # 구독 해지
  python manage.py sub count                    # 구독자 수

  python manage.py send --test                  # 테스트 발송 (config.yaml의 test_email)
  python manage.py send                         # 전체 구독자 발송
  python manage.py send --to user@email.com     # 특정 주소에 발송

  python manage.py history                      # 발송 이력
  python manage.py history --last 5             # 최근 5건

  python manage.py server                       # 구독 API 서버 (포트 5100)
"""
import sys, io, os, json, sqlite3, argparse
if not isinstance(sys.stdout, io.TextIOWrapper) or sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from datetime import datetime

import yaml
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "subscribers.db")
CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# ════════════════════════════════════════
# DATABASE
# ════════════════════════════════════════
def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("""CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        name TEXT DEFAULT '',
        subscribed_at TEXT NOT NULL,
        status TEXT DEFAULT 'active',
        token TEXT DEFAULT ''
    )""")
    db.execute("""CREATE TABLE IF NOT EXISTS send_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        sent_at TEXT NOT NULL,
        recipient_count INTEGER DEFAULT 0,
        report_file TEXT DEFAULT '',
        status TEXT DEFAULT 'sent'
    )""")
    db.commit()
    return db


def gen_token():
    import hashlib, time
    return hashlib.sha256(f"{time.time()}".encode()).hexdigest()[:24]


# ════════════════════════════════════════
# SUBSCRIBER COMMANDS
# ════════════════════════════════════════
def sub_list():
    db = get_db()
    rows = db.execute("SELECT * FROM subscribers WHERE status='active' ORDER BY subscribed_at DESC").fetchall()
    if not rows:
        print("  구독자 없음")
        return
    print(f"\n  {'Email':35s} {'Name':15s} {'Subscribed':20s}")
    print(f"  {'─'*35} {'─'*15} {'─'*20}")
    for r in rows:
        print(f"  {r['email']:35s} {r['name'] or '-':15s} {r['subscribed_at'][:16]:20s}")
    print(f"\n  Total: {len(rows)} active subscribers")
    db.close()


def sub_add(email, name=""):
    db = get_db()
    token = gen_token()
    try:
        db.execute("INSERT INTO subscribers (email, name, subscribed_at, status, token) VALUES (?, ?, ?, 'active', ?)",
                   (email.lower().strip(), name, datetime.now().isoformat(), token))
        db.commit()
        print(f"  Added: {email}")
    except sqlite3.IntegrityError:
        db.execute("UPDATE subscribers SET status='active', name=? WHERE email=?", (name, email.lower().strip()))
        db.commit()
        print(f"  Re-activated: {email}")
    db.close()


def sub_remove(email):
    db = get_db()
    db.execute("UPDATE subscribers SET status='unsubscribed' WHERE email=?", (email.lower().strip(),))
    db.commit()
    print(f"  Removed: {email}")
    db.close()


def sub_count():
    db = get_db()
    n = db.execute("SELECT COUNT(*) FROM subscribers WHERE status='active'").fetchone()[0]
    print(f"  Active subscribers: {n}")
    db.close()


# ════════════════════════════════════════
# SEND NEWSLETTER
# ════════════════════════════════════════
def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    mail = cfg.get("mail", {})
    if not mail.get("api_key") or mail["api_key"].startswith("${"):
        mail["api_key"] = os.environ.get("RESEND_API_KEY", "")
    return cfg


def build_email_html(week_range, unsub_url=""):
    """주간 리포트 데이터를 이메일 호환 HTML(테이블+인라인CSS)로 생성"""
    # Load stories data from weekly_report.py output
    data_path = os.path.join(OUTPUT_DIR, "data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        gdata = json.load(f)

    gdelt_total = gdata["stats"]["total_articles"]
    tmdb = gdata.get("tmdb", {})

    # 주간 스토리 (weekly_report.py와 동일한 데이터)
    stories = _get_weekly_stories()

    def esc(s):
        return (s or '').replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

    # ── Stories HTML (테이블 기반) ──
    stories_html = ""
    for i, s in enumerate(stories[:8]):
        color = s["color"]
        title = esc(s["title"])
        body = esc(s["body"][:300]) if i < 2 else esc(s["body"][:180])
        cat = s["category"]
        n = s["source_count"]
        url = s["sources"][0][1] if s["sources"] else "#"
        is_top = i == 0
        is_pick = i == 1

        # Key points
        kps_html = ""
        if s.get("key_points") and i < 2:
            kps_html = '<table cellpadding="0" cellspacing="0" border="0" style="margin:8px 0 8px 16px;"><tbody>'
            for kp in s["key_points"][:3]:
                kps_html += f'<tr><td style="padding:2px 0;font-size:13px;color:#555;line-height:1.6;">• {esc(kp)}</td></tr>'
            kps_html += '</tbody></table>'

        # Source links
        src_html = " · ".join(
            f'<a href="{u}" style="color:#1a6bff;text-decoration:none;font-size:12px;">{n_}</a>'
            for n_, u in s["sources"][:4]
        )

        # Image for top 2
        img_html = ""
        if s.get("image") and i < 2:
            img_html = f'''<tr><td style="padding:0;">
                <img src="{s["image"]}" width="560" style="width:100%;max-width:560px;height:auto;border-radius:8px 8px 0 0;display:block;" alt="">
            </td></tr>'''

        border_w = "4px" if i < 2 else "3px"
        title_sz = "20px" if is_top else "17px" if is_pick else "15px"
        body_sz = "15px" if i < 2 else "13px"
        label = " · TOP STORY" if is_top else " · EDITOR'S PICK" if is_pick else ""

        stories_html += f'''
        <tr><td style="padding:0 0 16px 0;">
          <table cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#ffffff;border-radius:8px;border-left:{border_w} solid {color};overflow:hidden;">
            {img_html}
            <tr><td style="padding:20px 24px;">
              <div style="font-size:11px;font-weight:700;color:{color};text-transform:uppercase;letter-spacing:0.5px;margin-bottom:6px;">
                {cat} · {n} sources{label}
              </div>
              <a href="{url}" style="font-size:{title_sz};font-weight:700;color:#111111;text-decoration:none;line-height:1.4;display:block;margin-bottom:8px;" target="_blank">{title}</a>
              <p style="font-size:{body_sz};color:#444444;line-height:1.7;margin:0 0 8px 0;">{body}</p>
              {kps_html}
              <div style="border-top:1px solid #eeeeee;padding-top:8px;margin-top:8px;">{src_html}</div>
            </td></tr>
          </table>
        </td></tr>'''

    # ── Policy Tracker ──
    policies = [
        ("🇺🇸🇨🇦", "C-11 vs 美 관세"),
        ("🇰🇷", "통합미디어법"),
        ("🇪🇺", "AVMSD 개정"),
        ("🇮🇳", "OTT 조사"),
        ("🇩🇪", "AI 저작권"),
    ]
    policy_html = '<tr><td style="padding:0;"><table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>'
    for flag, label in policies:
        policy_html += f'''<td width="20%" style="text-align:center;padding:12px 4px;background:#ffffff;border-radius:8px;">
            <div style="font-size:20px;margin-bottom:4px;">{flag}</div>
            <div style="font-size:11px;font-weight:700;color:#111;">{label}</div>
        </td>'''
    policy_html += '</tr></table></td></tr>'

    # ── TMDb ──
    tmdb_html = ""
    if tmdb.get("movies"):
        tmdb_html += '<tr><td style="padding:12px 0 0 0;"><table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>'
        for m in tmdb["movies"][:4]:
            poster = f"https://image.tmdb.org/t/p/w154{m['poster_path']}" if m.get("poster_path") else ""
            tmdb_html += f'''<td width="25%" style="text-align:center;padding:4px;">
                {"<img src='" + poster + "' width='80' style='border-radius:6px;' alt=''>" if poster else ""}
                <div style="font-size:11px;font-weight:600;margin-top:4px;color:#111;">{m.get('title','')[:20]}</div>
                <div style="font-size:10px;color:#888;">★ {m.get('vote_average',0):.1f}</div>
            </td>'''
        tmdb_html += '</tr></table></td></tr>'

    # ── Full Email ──
    email_html = f'''<!DOCTYPE html>
<html lang="ko">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>MediaINT Weekly Briefing</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/subsets/Paperlogy-dynamic-subset.css">
</head>
<body style="margin:0;padding:0;background:#f5f5f7;font-family:'Paperlogy',-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">

<table cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#f5f5f7;">
<tr><td align="center" style="padding:20px 16px;">

<table cellpadding="0" cellspacing="0" border="0" width="600" style="max-width:600px;width:100%;">

<!-- Header -->
<tr><td style="padding:24px 0;text-align:center;">
  <div style="display:inline-block;background:#1a6bff;color:#ffffff;padding:4px 14px;border-radius:20px;font-size:12px;font-weight:700;margin-bottom:8px;">WEEKLY REPORT</div><br>
  <div style="font-size:28px;font-weight:900;color:#111111;letter-spacing:-1px;">Media<span style="color:#1a6bff;">INT</span></div>
  <div style="font-size:13px;color:#888888;margin-top:4px;">{week_range} · {gdelt_total}+ articles analyzed</div>
</td></tr>

<!-- Stats -->
<tr><td style="padding:12px 20px;background:#ffffff;border-radius:8px;">
  <table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
    <td style="text-align:center;"><span style="font-size:18px;font-weight:700;color:#1a6bff;">{gdelt_total}</span><br><span style="font-size:10px;color:#888;text-transform:uppercase;">Articles</span></td>
    <td style="text-align:center;"><span style="font-size:18px;font-weight:700;color:#1a6bff;">{len(stories)}</span><br><span style="font-size:10px;color:#888;text-transform:uppercase;">Stories</span></td>
    <td style="text-align:center;"><span style="font-size:18px;font-weight:700;color:#1a6bff;">5</span><br><span style="font-size:10px;color:#888;text-transform:uppercase;">Policy</span></td>
    <td style="text-align:center;"><span style="font-size:18px;font-weight:700;color:#1a6bff;">4</span><br><span style="font-size:10px;color:#888;text-transform:uppercase;">Regions</span></td>
  </tr></table>
</td></tr>

<tr><td style="height:16px;"></td></tr>

<!-- Stories -->
<tr><td style="font-size:11px;font-weight:800;color:#888888;letter-spacing:1.5px;padding:0 0 8px 0;border-bottom:2px solid #111111;">THIS WEEK'S STORIES</td></tr>
<tr><td style="height:12px;"></td></tr>
{stories_html}

<!-- Policy -->
<tr><td style="font-size:11px;font-weight:800;color:#888888;letter-spacing:1.5px;padding:16px 0 8px 0;border-bottom:2px solid #111111;">GLOBAL POLICY TRACKER</td></tr>
<tr><td style="height:8px;"></td></tr>
{policy_html}

<!-- Trending -->
{"<tr><td style='font-size:11px;font-weight:800;color:#888888;letter-spacing:1.5px;padding:16px 0 8px 0;border-bottom:2px solid #111111;'>TRENDING ENTERTAINMENT</td></tr>" + tmdb_html if tmdb_html else ""}

<!-- CTA -->
<tr><td style="padding:24px 0;text-align:center;">
  <a href="https://kimyonghee.com/mediaint" style="display:inline-block;background:#1a6bff;color:#ffffff;padding:12px 32px;border-radius:8px;font-size:14px;font-weight:700;text-decoration:none;">전체 리포트 보기</a>
</td></tr>

<!-- Footer -->
<tr><td style="text-align:center;padding:24px 0;color:#bbbbbb;font-size:11px;line-height:1.6;">
  MediaINT Weekly Briefing · Powered by GDELT + TMDb + Claude Agent<br>
  <a href="https://kimyonghee.com/mediaint" style="color:#1a6bff;text-decoration:none;">kimyonghee.com</a><br>
  <a href="{unsub_url or '#'}" style="color:#bbbbbb;font-size:10px;">구독 해지</a>
</td></tr>

</table>
</td></tr></table>
</body></html>'''

    return email_html


def _get_weekly_stories():
    """stories_weekly.json에서 스토리 로드"""
    stories_path = os.path.join(BASE_DIR, "stories_weekly.json")
    with open(stories_path, "r", encoding="utf-8") as f:
        stories = json.load(f)
    for s in stories:
        s["sources"] = [tuple(x) for x in s["sources"]]
    return stories

def _get_weekly_stories_old():
    """이전 하드코딩 데이터 (참조용)"""
    return [
        {
            "rank": 1,
            "title": "파라마운트-WBD, $1,100억 합병 합의…할리우드 판도 재편",
            "category": "Media Business",
            "color": "#1565c0",
            "body": "파라마운트 스카이댄스가 워너브라더스 디스커버리(WBD)를 주당 31달러, 기업가치 1,100억 달러에 인수하는 합병 계약을 체결했다. 이번 거래로 HBO Max와 Paramount+가 통합되면 구독자 2억 명 규모의 초대형 스트리밍 플랫폼이 탄생한다. 넷플릭스가 먼저 WBD 인수를 추진했으나, 파라마운트 스카이댄스가 2025년 12월 역제안을 내놓으며 경쟁 입찰 구도로 전환. 결국 넷플릭스가 가격 경쟁을 포기하면서 파라마운트에 낙찰되었다. 합병 후 Game of Thrones, DC 유니버스, 미션 임파서블, 탑건, 해리포터, 스폰지밥 등 양사의 IP 포트폴리오가 통합되며, 연간 극장 개봉작 30편을 편성하는 할리우드 최대 콘텐츠 하우스가 출범하게 된다.",
            "key_points": [
                "파라마운트, WBD 주당 31달러·기업가치 $1,100억에 인수 합의",
                "HBO Max + Paramount+ 통합으로 구독자 2억 돌파 전망",
                "Game of Thrones·DC·미션 임파서블 등 IP 통합, 연간 극장 30편 편성 계획"
            ],
            "sources": [
                ("Paramount Press", "https://www.paramount.com/press/paramount-to-acquire-warner-bros-discovery-to-form-next-generation-global-media-and-entertainment-company"),
                ("Deadline", "https://deadline.com/2026/03/paramount-warner-bros-merger-movie-release-plans-1236739301/"),
                ("PBS News", "https://www.pbs.org/newshour/show/the-concerns-and-implications-of-paramounts-warner-bros-buyout"),
                ("Yale Insights", "https://insights.som.yale.edu/insights/what-the-paramount-warner-bros-merger-means-for-streaming"),
            ],
            "source_count": 42,
            "image": "https://media-cldnry.s-nbcnews.com/image/upload/t_social_share_1024x768_scale,f_auto,q_auto:best/rockcms/2025-09/250904-paramount-studios-ew-315p-532e5d.jpg",
        },
        {
            "rank": 2,
            "title": "BTS, 넷플릭스 동시접속 1,840만 신기록…'ARIRANG' 콘서트 전 세계 열광",
            "category": "K-Content",
            "color": "#d81b60",
            "body": "BTS가 4년 만의 완전체 컴백 콘서트 'BTS THE COMEBACK LIVE | ARIRANG'으로 서울 광화문 일대를 마비시켰다. 3월 21일 넷플릭스 글로벌 생중계에 1,840만 명이 동시 접속해 플랫폼 역대 최다 기록을 경신했으며, 24개국에서 1위, 80개국 주간 톱10에 진입했다. 군 복무를 마치고 4년 만에 재결합한 7인조는 신보 'ARIRANG'으로 스포티파이 첫날 1억 1,000만 스트림을 기록, 2026년 최고 데뷔 성적을 달성했다.",
            "key_points": [
                "넷플릭스 라이브 동시접속 1,840만, 플랫폼 역대 최다 기록 경신",
                "광화문 콘서트 26만 관객 동원, 서울 도심 전면 통제",
                "컴백 앨범 첫날 390만 장 판매, 지미 팰런 쇼 구겐하임 미술관 공연"
            ],
            "sources": [
                ("Netflix Tudum", "https://www.netflix.com/tudum/features/bts-comeback-live-arirang-recap-highlights"),
                ("Billboard", "https://www.billboard.com/music/pop/bts-comeback-live-18-4-million-views-netflix-1236206297/"),
                ("Variety", "https://variety.com/2026/tv/news/bts-the-comeback-live-arirang-ratings-netflix-1236698023/"),
                ("CNN", "https://www.cnn.com/2026/03/21/style/bts-arirang-comeback-concert-korea-intl-hnk"),
            ],
            "source_count": 28,
            "image": "https://dnm.nflximg.net/api/v6/BvVbc2Wxr2w6QuoANoSpJKEIWjQ/AAAAQaefV-1USGIxOOstlJzpNR3fB6kQnglV7qVpXI85GkbZbWqaInafomENEfJ6Eq6wJG_6FuSTYyEziFYZn8uHRY1lVgieQmyLIaCHhStj_A8bLfqefzIjoDhnZLyQjPvud2WZ6bZ_QTUmyfzHGAeP1xd0.jpg?r=d10",
        },
        {
            "rank": 3,
            "title": "캐나다 온라인 스트리밍법, 美 의회 관세 위협 직면",
            "category": "Regulation",
            "color": "#ff6f00",
            "body": "넷플릭스 등 스트리밍 사업자에 캐나다 콘텐츠 제작 투자를 의무화하는 캐나다 온라인 스트리밍법(C-11)이 미국 공화당의 표적이 되었다. 로이드 스머커 의원이 미국 기업 차별 여부를 조사하는 법안을 발의했으며, 관세 조치로 이어질 수 있다는 관측이 나온다.",
            "key_points": [],
            "sources": [("The Globe and Mail", "https://www.theglobeandmail.com/politics/article-online-streaming-act-us-republican-congress-tariffs/")],
            "source_count": 8, "image": "",
        },
        {
            "rank": 4,
            "title": "한국, 방송·OTT·유튜브 아우르는 통합미디어법 논의 본격화",
            "category": "Regulation",
            "color": "#ff6f00",
            "body": "기존 매체 중심 규제에서 벗어나 '시청각미디어서비스' 개념을 기준으로 방송, OTT, 유튜브를 하나의 법적 틀로 묶는 통합미디어법 논의가 본격화했다. 서비스의 사회적 영향력에 따라 규제 강도를 차등 적용하는 방향.",
            "key_points": [],
            "sources": [("다음뉴스", "https://v.daum.net/v/20260126145411885"), ("전자신문", "https://www.etnews.com/20260312000341")],
            "source_count": 12, "image": "",
        },
        {
            "rank": 5,
            "title": "ByteDance, AI 영상생성 'SeeDance 2.0' 글로벌 출시",
            "category": "OTT/Streaming",
            "color": "#e53935",
            "body": "바이트댄스가 AI 기반 영상 생성 모델 SeeDance 2.0을 전 세계에 조용히 출시했다. 텍스트-투-비디오, 이미지-투-비디오 기능을 탑재해 크리에이터 경제의 제작 비용을 획기적으로 낮출 수 있는 도구로 평가.",
            "key_points": [],
            "sources": [("TechCrunch", "#")],
            "source_count": 6, "image": "",
        },
        {
            "rank": 6,
            "title": "EU, 시청각미디어서비스지침(AVMSD) 2026년 전면 개정 착수",
            "category": "Regulation",
            "color": "#ff6f00",
            "body": "유럽위원회가 AVMSD의 사후평가를 위한 증거 수집에 착수했다. 스트리밍 플랫폼의 유럽 콘텐츠 쿼터, 아동 프라이버시 보호, AI 생성 콘텐츠 규제 등이 핵심 의제로 부상.",
            "key_points": [],
            "sources": [("Inside Global Tech", "https://www.insideglobaltech.com/2025/12/01/the-european-commission-calls-for-evidence-ahead-of-its-2026-evaluation-and-review-of-the-audiovisual-media-services-directive/")],
            "source_count": 5, "image": "",
        },
        {
            "rank": 7,
            "title": "인도 의회, OTT 플랫폼 10~15곳 '불법 콘텐츠' 조사 착수",
            "category": "Regulation",
            "color": "#ff6f00",
            "body": "인도 의회 정보통신상임위원회가 OTT 플랫폼의 규제 공백을 지적하며 10~15개 플랫폼을 대상으로 불법·선정적 콘텐츠 유통 실태 조사에 착수했다.",
            "key_points": [],
            "sources": [("Storyboard18", "https://www.storyboard18.com/amp/brand-makers/parliamentary-panel-flags-ott-regulatory-gaps-10-15-platforms-under-examination-92510.htm")],
            "source_count": 4, "image": "",
        },
        {
            "rank": 8,
            "title": "Disney+, '데어데블: 본 어게인' 시즌2 공개…마블 구원투수 기대",
            "category": "OTT/Streaming",
            "color": "#e53935",
            "body": "디즈니+가 '데어데블: 본 어게인' 시즌2를 3월 24일 공개하며 크리스틴 리터의 제시카 존스를 MCU에 복귀시켰다. 실사 '신데렐라' 스핀오프 '스텝시스터스' 제작도 발표.",
            "key_points": [],
            "sources": [("Tom's Guide", "https://www.tomsguide.com/entertainment/streaming/5-top-new-shows-you-can-stream-this-week-on-netflix-disney-and-more-march-23-29")],
            "source_count": 15, "image": "",
        },
    ]


def send_newsletter(recipients, test_mode=False):
    cfg = load_config()
    mail_cfg = cfg.get("mail", {})
    api_key = mail_cfg.get("api_key", "")
    from_addr = mail_cfg.get("from", "")
    provider = mail_cfg.get("provider", "resend")
    name = cfg.get("name", "MediaINT")

    ts = datetime.now().strftime("%Y-%m-%d")
    subject = f"{name} Weekly Briefing — {ts}"

    week_range = "2026.03.20 — 03.26"
    email_html = build_email_html(week_range)

    mode_label = "TEST" if test_mode else "SEND"
    print(f"\n  [{mode_label}] Subject: {subject}")
    print(f"  [{mode_label}] Recipients: {len(recipients)}")
    print(f"  [{mode_label}] Provider: {provider}")

    if not api_key or api_key.startswith("YOUR_"):
        print(f"\n  Error: API key not configured in config.yaml")
        print(f"  Set mail.api_key in {CONFIG_PATH}")
        return

    if not from_addr or from_addr.startswith("MediaINT <mediaint@your"):
        print(f"\n  Error: From address not configured in config.yaml")
        return

    sent = 0
    failed = 0

    if provider == "resend":
        for email in recipients:
            try:
                r = requests.post("https://api.resend.com/emails", headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }, json={
                    "from": from_addr,
                    "to": [email],
                    "subject": subject,
                    "html": email_html,
                })
                if r.status_code == 200:
                    print(f"    Sent: {email}")
                    sent += 1
                else:
                    print(f"    Failed: {email} ({r.status_code})")
                    failed += 1
            except Exception as e:
                print(f"    Error: {email} ({e})")
                failed += 1

    elif provider == "smtp":
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        smtp_host = mail_cfg.get("smtp_host", "smtp.gmail.com")
        smtp_port = mail_cfg.get("smtp_port", 587)
        smtp_user = mail_cfg.get("smtp_user", "")
        smtp_pass = mail_cfg.get("smtp_pass", "")

        try:
            server = smtplib.SMTP(smtp_host, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_pass)

            for email in recipients:
                msg = MIMEMultipart("alternative")
                msg["Subject"] = subject
                msg["From"] = from_addr or smtp_user
                msg["To"] = email
                msg.attach(MIMEText(email_html, "html", "utf-8"))
                server.send_message(msg)
                print(f"    Sent: {email}")
                sent += 1

            server.quit()
        except Exception as e:
            print(f"    SMTP error: {e}")
            failed = len(recipients)

    # Record history
    db = get_db()
    db.execute("INSERT INTO send_history (subject, sent_at, recipient_count, report_file, status) VALUES (?, ?, ?, ?, ?)",
               (subject, datetime.now().isoformat(), sent, f"weekly_{ts}.html", "sent" if failed == 0 else "partial"))
    db.commit()
    db.close()

    print(f"\n  Done! Sent: {sent}, Failed: {failed}")


def cmd_send(args):
    cfg = load_config()
    mail_cfg = cfg.get("mail", {})

    if args.to:
        recipients = [args.to]
        send_newsletter(recipients)
    elif args.test:
        test_email = mail_cfg.get("test_email", "")
        if not test_email:
            print("  Error: test_email not set in config.yaml")
            return
        send_newsletter([test_email], test_mode=True)
    else:
        # Send to all active subscribers from DB
        db = get_db()
        rows = db.execute("SELECT email FROM subscribers WHERE status='active'").fetchall()
        db.close()
        if not rows:
            print("  No active subscribers. Use: python manage.py sub add <email>")
            return
        recipients = [r["email"] for r in rows]
        confirm = input(f"  Send to {len(recipients)} subscribers? (y/N): ")
        if confirm.lower() != 'y':
            print("  Cancelled.")
            return
        send_newsletter(recipients)


# ════════════════════════════════════════
# HISTORY
# ════════════════════════════════════════
def show_history(limit=10):
    db = get_db()
    rows = db.execute("SELECT * FROM send_history ORDER BY sent_at DESC LIMIT ?", (limit,)).fetchall()
    if not rows:
        print("  발송 이력 없음")
        return
    print(f"\n  {'Date':20s} {'Subject':40s} {'Recipients':10s} {'Status':8s}")
    print(f"  {'─'*20} {'─'*40} {'─'*10} {'─'*8}")
    for r in rows:
        print(f"  {r['sent_at'][:16]:20s} {r['subject'][:40]:40s} {r['recipient_count']:>10d} {r['status']:8s}")
    db.close()


# ════════════════════════════════════════
# API SERVER (for kimyonghee.com integration)
# ════════════════════════════════════════
def run_server(port=5100):
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import urllib.parse

    class Handler(BaseHTTPRequestHandler):
        def _cors(self):
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")

        def do_OPTIONS(self):
            self.send_response(200)
            self._cors()
            self.end_headers()

        def do_POST(self):
            if self.path == "/subscribe":
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length).decode("utf-8")

                try:
                    data = json.loads(body)
                except:
                    data = dict(urllib.parse.parse_qsl(body))

                email = data.get("email", "").strip().lower()
                name = data.get("name", "")

                if not email or "@" not in email:
                    self.send_response(400)
                    self._cors()
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Invalid email"}).encode())
                    return

                db = get_db()
                token = gen_token()
                try:
                    db.execute("INSERT INTO subscribers (email, name, subscribed_at, status, token) VALUES (?, ?, ?, 'active', ?)",
                               (email, name, datetime.now().isoformat(), token))
                    db.commit()
                    msg = "Subscribed successfully"
                except sqlite3.IntegrityError:
                    db.execute("UPDATE subscribers SET status='active', name=? WHERE email=?", (name, email))
                    db.commit()
                    msg = "Re-activated subscription"
                db.close()

                self.send_response(200)
                self._cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "message": msg}).encode())
                print(f"  [Subscribe] {email}")

            elif self.path.startswith("/unsubscribe"):
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length).decode("utf-8") if length else ""
                try:
                    data = json.loads(body) if body else {}
                except:
                    data = {}

                token = data.get("token", "")
                db = get_db()
                if token:
                    db.execute("UPDATE subscribers SET status='unsubscribed' WHERE token=?", (token,))
                db.commit()
                db.close()

                self.send_response(200)
                self._cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "message": "Unsubscribed"}).encode())
            else:
                self.send_response(404)
                self.end_headers()

        def do_GET(self):
            if self.path == "/subscribe":
                # 간단한 구독 폼 HTML 반환
                html = """<!DOCTYPE html><html><head><meta charset="UTF-8">
                <style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:Inter,sans-serif;background:#f5f5f7;display:flex;justify-content:center;align-items:center;min-height:100vh}
                .box{background:#fff;border-radius:12px;padding:2.5rem;max-width:420px;width:100%;box-shadow:0 2px 16px rgba(0,0,0,.06)}
                h2{font-size:1.4rem;font-weight:800;margin-bottom:.3rem}h2 b{color:#1a6bff}
                p{font-size:.85rem;color:#888;margin-bottom:1.5rem}
                input{width:100%;padding:.75rem 1rem;border:1px solid #ddd;border-radius:8px;font-size:.9rem;margin-bottom:.75rem;outline:none}input:focus{border-color:#1a6bff}
                button{width:100%;padding:.75rem;background:#1a6bff;color:#fff;border:none;border-radius:8px;font-size:.9rem;font-weight:700;cursor:pointer}button:hover{background:#1454cc}
                .msg{text-align:center;padding:1rem;font-size:.85rem;color:#2e7d32;display:none}
                </style></head><body>
                <div class="box">
                <h2>Media<b>INT</b> Weekly</h2>
                <p>미디어 산업 인텔리전스를 매주 이메일로 받아보세요.</p>
                <form id="f">
                <input type="text" name="name" placeholder="이름 (선택)">
                <input type="email" name="email" placeholder="이메일 주소" required>
                <button type="submit">구독하기</button>
                </form>
                <div class="msg" id="msg"></div>
                <script>
                document.getElementById('f').onsubmit=async function(e){
                  e.preventDefault();
                  const d=new FormData(this);
                  const r=await fetch('/subscribe',{method:'POST',headers:{'Content-Type':'application/json'},
                    body:JSON.stringify({email:d.get('email'),name:d.get('name')})});
                  const j=await r.json();
                  document.getElementById('msg').style.display='block';
                  document.getElementById('msg').textContent=j.success?'구독 완료! 감사합니다.':'오류가 발생했습니다.';
                  if(j.success)this.reset();
                };
                </script></div></body></html>"""
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html.encode("utf-8"))

            elif self.path == "/stats":
                db = get_db()
                n = db.execute("SELECT COUNT(*) FROM subscribers WHERE status='active'").fetchone()[0]
                h = db.execute("SELECT COUNT(*) FROM send_history").fetchone()[0]
                db.close()
                self.send_response(200)
                self._cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"subscribers": n, "sends": h}).encode())
            else:
                self.send_response(404)
                self.end_headers()

        def log_message(self, format, *args):
            pass  # Suppress default logging

    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"\n  MediaINT Newsletter API Server")
    print(f"  http://localhost:{port}/subscribe  — 구독 폼")
    print(f"  POST /subscribe                    — 구독 API")
    print(f"  POST /unsubscribe                  — 해지 API")
    print(f"  GET  /stats                        — 통계")
    print(f"\n  Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")


# ════════════════════════════════════════
# CLI ENTRY POINT
# ════════════════════════════════════════
def main():
    parser = argparse.ArgumentParser(description="MediaINT Newsletter Manager")
    subparsers = parser.add_subparsers(dest="command")

    # sub commands
    sub_parser = subparsers.add_parser("sub", help="Subscriber management")
    sub_parser.add_argument("action", choices=["list", "add", "remove", "count"])
    sub_parser.add_argument("email", nargs="?", default="")
    sub_parser.add_argument("name", nargs="?", default="")

    # send command
    send_parser = subparsers.add_parser("send", help="Send newsletter")
    send_parser.add_argument("--test", action="store_true", help="Send to test_email only")
    send_parser.add_argument("--to", default="", help="Send to specific email")

    # history command
    hist_parser = subparsers.add_parser("history", help="Send history")
    hist_parser.add_argument("--last", type=int, default=10)

    # server command
    srv_parser = subparsers.add_parser("server", help="Run subscription API server")
    srv_parser.add_argument("--port", type=int, default=5100)

    args = parser.parse_args()

    if args.command == "sub":
        if args.action == "list":
            sub_list()
        elif args.action == "add":
            if not args.email:
                print("  Usage: python manage.py sub add <email> [name]")
                return
            sub_add(args.email, args.name)
        elif args.action == "remove":
            if not args.email:
                print("  Usage: python manage.py sub remove <email>")
                return
            sub_remove(args.email)
        elif args.action == "count":
            sub_count()

    elif args.command == "send":
        cmd_send(args)

    elif args.command == "history":
        show_history(args.last)

    elif args.command == "server":
        run_server(args.port)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
