import streamlit as st

st.set_page_config(page_title="여행 숙소 성향 테스트", page_icon="🧳", layout="wide")

st.markdown("""
<style>
.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
    font-size: 28px;
}

h2 { font-size: 48px !important; margin-top: 8px !important; }
h3 { font-size: 40px !important; }

div[role="radiogroup"] {
    gap: 48px;
    justify-content: center;
    padding: 8px 0 4px 0;
}
div[role="radiogroup"] label {
    font-size: 36px !important;
    font-weight: 700;
    transition: transform 0.15s ease;
}
div[role="radiogroup"] label:hover { transform: scale(1.25); }
div[role="radiogroup"] label p { font-size: 36px !important; }

div[data-testid="stVerticalBlockBorderWrapper"] {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    border-radius: 18px;
    padding: 12px 18px;
    margin-bottom: 22px;
}
div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 14px 30px rgba(102, 126, 234, 0.20);
}

.q-title    { font-size: 46px !important; font-weight: 800; margin: 6px 0 14px 0; }
.q-title-p2 { font-size: 46px !important; font-weight: 800; margin: 6px 0 14px 0; }
.q-desc     { font-size: 32px !important; line-height: 1.7; color: #4a4a5a; margin-bottom: 18px; }

.anchor-wrap { display: flex; gap: 18px; margin: 6px 0 16px 0; }
.anchor {
    flex: 1; padding: 16px 20px; border-radius: 14px;
    font-size: 26px !important; line-height: 1.5;
}
.anchor .num { font-weight: 800; font-size: 26px !important; }
.anchor.low  { background: #eef1ff; color: #4453b8; }
.anchor.high { background: #f6eeff; color: #7a3fb0; }

.banner {
    background: linear-gradient(270deg, #667eea, #764ba2, #6a82fb, #764ba2);
    background-size: 600% 600%;
    animation: gradientShift 10s ease infinite;
    border-radius: 24px;
    padding: 60px 40px;
    text-align: center;
    color: white;
    margin-bottom: 16px;
}
.banner h1 { color: white; font-size: 60px; margin: 0 0 16px 0; }
.banner p  { color: #e8e6ff; font-size: 30px; margin: 0; }
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.result-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 24px;
    padding: 56px 40px;
    text-align: center;
    color: white;
    margin: 20px 0;
    animation: popIn 0.6s cubic-bezier(0.18, 0.89, 0.32, 1.28);
}
.result-card .code { font-size: 28px !important; letter-spacing: 8px; opacity: 0.85; }
.result-card .name { font-size: 64px !important; font-weight: 800; margin: 16px 0; }
.result-card .desc { font-size: 30px !important; line-height: 1.8; color: #f0eeff; max-width: 820px; margin: 0 auto; }
@keyframes popIn {
    0%   { opacity: 0; transform: scale(0.85) translateY(24px); }
    100% { opacity: 1; transform: scale(1)    translateY(0); }
}

.gauge-row   { display: flex; align-items: center; gap: 18px; margin: 22px 0; }
.gauge-label { width: 160px; font-size: 28px !important; font-weight: 700; }
.gauge-label.right { text-align: left; }
.gauge-label.left  { text-align: right; }
.gauge-bar {
    flex: 1; height: 34px; border-radius: 17px;
    background: #e9e6f7; overflow: hidden; display: flex;
}
.gauge-fill {
    background: linear-gradient(90deg, #667eea, #764ba2);
    height: 100%; border-radius: 17px;
    animation: fillUp 1.2s ease-out;
}
.gauge-pct { width: 80px; font-size: 28px !important; font-weight: 800; color: #667eea; }
@keyframes fillUp { from { width: 0; } }

.progress-text { font-size: 28px !important; font-weight: 700; color: #667eea; }
</style>
""", unsafe_allow_html=True)

TYPE_INFO = {
    "ELRC": ("🎯 알뜰 플래너", "가성비도 챙기고 일정도 미리 짜두는 실속파. 잘 알아보고 예약한 숙소에서 푹 쉬는 걸 좋아해요.", "리뷰 많은 검증된 가성비 호텔을 미리 예약하기"),
    "ELRS": ("🎲 자유로운 절약가", "싸고 편하면 그걸로 충분! 굳이 미리 정하지 않고 그때그때 끌리는 곳으로 떠나요.", "게스트하우스나 저가 숙소, 당일 특가 노려보기"),
    "ELAC": ("🏃 부지런한 탐험가", "예산은 아끼되 동선은 알차게. 가성비 숙소를 베이스캠프 삼아 부지런히 돌아다녀요.", "위치 좋은 가성비 숙소 + 빽빽한 일정 미리 짜두기"),
    "ELAS": ("🌀 즉흥 백패커", "계획보다 몸이 먼저! 잠만 잘 수 있으면 어디든 OK인 자유로운 타입이에요.", "도미토리나 저가 숙소, 현지에서 즉흥적으로 정하기"),
    "EVRC": ("🌙 감성 힐링러", "분위기 좋은 곳을 미리 찾아두고 조용히 쉬러 가는 타입. 가성비도 놓치지 않아요.", "감성 있는 숙소를 미리 알아보고 예약하기"),
    "EVRS": ("🍃 감성 유랑자", "끌리는 분위기를 따라 발길 닿는 대로. 예쁘면 가격은 좀 덜 따지는 편이에요.", "그때그때 마음에 드는 감성 숙소로 즉흥 예약하기"),
    "EVAC": ("📸 감성 투어리스트", "예쁜 곳은 다 가봐야 직성이 풀리는 타입. 포토스팟을 미리 찾아두고 부지런히 움직여요.", "사진 잘 나오는 감성 숙소 미리 리스트업하기"),
    "EVAS": ("🎨 자유 감성파", "분위기가 좋으면 일정도 즉석에서 바꾸는 타입. 감성 가는 대로 움직여요.", "분위기 보고 즉석에서 정하는 감성 숙소"),
    "PLRC": ("💼 비즈니스 트래블러", "좋은 호텔을 미리 잡아두고 컨디션 관리를 우선하는 타입. 깔끔하고 효율적인 여행을 좋아해요.", "위치·서비스 좋은 프리미엄 호텔 미리 예약하기"),
    "PLRS": ("🛋️ 럭셔리 휴양객", "좋은 숙소에서 즉흥적으로 늘어지는 게 최고. 미리 정하기보단 끌리는 대로 가요.", "고급 리조트에서 즉흥 호캉스 즐기기"),
    "PLAC": ("🗺️ 프리미엄 탐험가", "좋은 숙소에 꼼꼼한 일정까지. 편안함과 알찬 동선을 둘 다 챙기는 타입이에요.", "위치 좋은 고급 숙소 + 알찬 일정 준비하기"),
    "PLAS": ("⚡ 럭셔리 즉흥러", "비싸도 좋으면 일단 가자! 계획 없이도 좋은 곳으로 떠나는 타입이에요.", "끌리는 고급 숙소로 즉흥 예약하기"),
    "PVRC": ("💑 로맨틱 플래너", "분위기 좋은 곳을 철저히 준비해서 여유롭게 쉬는 타입. 특별한 날을 잘 챙겨요.", "분위기 좋은 호텔을 미리 예약해 기념일 준비하기"),
    "PVRS": ("🥂 무드 헤도니스트", "분위기에 취해 즉흥적으로 호캉스를 떠나는 타입. 그 순간의 무드가 제일 중요해요.", "감성 가득한 숙소에서 즉흥 호캉스 즐기기"),
    "PVAC": ("👑 완벽주의 큐레이터", "모든 걸 완벽하게 준비하는 여행 장인. 분위기와 동선을 빈틈없이 챙겨요.", "감성과 위치 모두 완벽한 숙소 미리 확정하기"),
    "PVAS": ("✨ 럭셔리 무드메이커", "그날의 분위기를 따라 고급스럽게 즉흥 여행. 멋과 자유로움을 둘 다 잡아요.", "분위기 따라 고르는 고급 숙소로 즉흥 여행하기"),
}

SCALE = [1, 2, 3, 4, 5]

def get_dimensions(price, service, location, vibe, q3_1, q3_2, q4_1, q4_2):
    dims = []
    pct_e = price / (price + service) * 100
    dims.append(("E" if pct_e >= 50 else "P", pct_e, "💰 가성비", "✨ 프리미엄"))
    pct_l = location / (location + vibe) * 100
    dims.append(("L" if pct_l >= 50 else "V", pct_l, "📍 효율", "🌿 감성"))
    act = (q3_1 + q3_2) / 2
    pct_r = (act - 1) / 4 * 100
    dims.append(("R" if pct_r >= 50 else "A", pct_r, "🛋️ 휴식", "🏃 액티브"))
    plan = (q4_1 + q4_2) / 2
    pct_c = (plan - 1) / 4 * 100
    dims.append(("C" if pct_c >= 50 else "S", pct_c, "🗓️ 계획", "🎲 즉흥"))
    return dims

def gauge_html(left_label, right_label, left_pct):
    return f"""
    <div class="gauge-row">
        <span class="gauge-label left">{left_label}</span>
        <div class="gauge-bar"><div class="gauge-fill" style="width:{left_pct:.0f}%"></div></div>
        <span class="gauge-label right">{right_label}</span>
        <span class="gauge-pct">{max(left_pct, 100-left_pct):.0f}%</span>
    </div>"""

def comfort_note(sleep, hygiene):
    notes = []
    if sleep >= 4:
        notes.append("잠자리가 편해야 여행이 산다고 느끼는 편이네요. 침구랑 방음 후기를 꼭 챙겨보세요.")
    elif sleep <= 2:
        notes.append("잠자리에는 크게 예민하지 않아서 고를 수 있는 숙소가 훨씬 넓어요.")
    if hygiene >= 4:
        notes.append("위생은 절대 양보 못 하는 편! 청결 평점이 높은 곳 위주로 보면 좋아요.")
    elif hygiene <= 2:
        notes.append("위생은 어느 정도 감수하는 편이라 개성 있는 숙소도 도전해볼 만해요.")
    if not notes:
        notes.append("수면도 위생도 적당히 보는 편이라, 무난하고 균형 잡힌 선택을 하겠네요.")
    return " ".join(notes)

# ── 헤더 ──
st.markdown("""
<div class="banner">
    <h1>🧳 여행 숙소 성향 테스트</h1>
    <p>10개의 질문으로 알아보는 나의 여행 유형 — 당신은 16가지 중 어떤 여행자인가요?</p>
</div>
""", unsafe_allow_html=True)
st.write("")

# ── PART 1 ──
st.markdown('<h2>PART 1 · 숙소를 고르는 기준</h2><p class="q-desc">아래 항목들이 숙소를 고를 때 각각 얼마나 중요한지 1점(전혀 안 중요)부터 5점(아주 중요)까지 골라주세요.</p>', unsafe_allow_html=True)

questions_part1 = [
    ("💸 가격", "여행 예산에서 숙소 비용을 얼마나 신경 쓰나요? 같은 동네라면 단돈 몇 천 원이라도 더 저렴한 곳을 찾아보는 편인지, 가격표보다 다른 조건을 먼저 보는 편인지 떠올려 보세요."),
    ("🛎️ 서비스", "체크인할 때의 친절함, 짐을 들어주는 직원, 룸서비스, 조식 퀄리티처럼 '사람이 챙겨주는 경험'이 숙소 만족도를 크게 좌우하나요?"),
    ("📍 위치", "관광지나 지하철역까지의 거리, 주변 편의시설처럼 '동선의 편리함'이 숙소 선택의 핵심인가요? 외곽이라도 괜찮은지, 무조건 중심가여야 하는지 생각해 보세요."),
    ("✨ 분위기", "인테리어, 조명, 창밖 뷰, 감성적인 공간 연출처럼 '예쁘고 무드 있는 곳'에 끌리나요? 사진이 잘 나오는 숙소인지가 중요한지요."),
    ("😴 수면의 질", "매트리스와 침구의 편안함, 방음, 암막 커튼처럼 '잘 자는 환경'을 따지나요? 자고 일어났을 때의 개운함이 여행 컨디션을 좌우하는 편인지요."),
    ("🧼 위생", "객실 청소 상태, 욕실과 침구의 청결, 냄새나 곰팡이 여부처럼 '깨끗함'이 절대 기준인가요? 조금이라도 더러우면 다시 안 가는 편인지요."),
]

answers1 = {}
for title, desc in questions_part1:
    with st.container(border=True):
        st.markdown(f'<p class="q-title">{title}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="q-desc">{desc}</p>', unsafe_allow_html=True)
        answers1[title] = st.radio(title, SCALE, index=None, horizontal=True, label_visibility="collapsed")

price, service = answers1["💸 가격"], answers1["🛎️ 서비스"]
location, vibe = answers1["📍 위치"], answers1["✨ 분위기"]
sleep, hygiene = answers1["😴 수면의 질"], answers1["🧼 위생"]

st.write("")

# ── PART 2 ──
st.markdown('<h2>PART 2 · 나의 여행 스타일</h2><p class="q-desc">정답은 없어요. 양쪽 설명을 읽고, 평소 내 모습과 가까운 쪽으로 점수를 골라주세요. (1점=왼쪽 / 5점=오른쪽)</p>', unsafe_allow_html=True)

questions_part2 = [
    ("q3_1", "🛋️ 나에게 숙소란?",
     "숙소는 그냥 잠만 자는 곳이에요. 여행은 밖에서 즐기는 거고, 방은 깨끗하게 눈만 붙이면 충분해요.",
     "숙소가 여행의 핵심이에요. 좋은 방에서 최대한 오래 머물며 그 공간 자체를 즐기고 싶어요."),
    ("q3_2", "🛌 여행에 '쉬는 시간'이 필요한가요?",
     "일정은 알차게 꽉 채우는 게 좋아요. 기껏 왔는데 쉬면 시간이 아까워요.",
     "멍 때리고 아무것도 안 하는 시간이 꼭 있어야 해요. 그래야 진짜 쉬는 느낌이 들어요."),
    ("q4_1", "🗓️ 여행 일정은 어떻게 짜나요?",
     "일단 떠나고, 가서 그때그때 정해요. 너무 빡빡한 계획은 답답해요.",
     "출발 전에 숙소·맛집·동선까지 거의 다 정해둬요. 준비된 여행이 마음 편해요."),
    ("q4_2", "🎲 예상 못 한 일이 생기면?",
     "식당이 문 닫았거나 날씨가 바뀌어도 괜찮아요. 오히려 그런 변수가 여행의 묘미죠.",
     "계획이 틀어지면 당황스럽고 불편해요. 대비책까지 챙겨두는 편이에요."),
]

answers2 = {}
for key, title, low, high in questions_part2:
    with st.container(border=True):
        st.markdown(f'<p class="q-title-p2">{title}</p>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="anchor-wrap">
            <div class="anchor low"><span class="num">1점</span> · {low}</div>
            <div class="anchor high"><span class="num">5점</span> · {high}</div>
        </div>
        """, unsafe_allow_html=True)
        answers2[key] = st.radio(key, SCALE, index=None, horizontal=True, label_visibility="collapsed")

q3_1, q3_2 = answers2["q3_1"], answers2["q3_2"]
q4_1, q4_2 = answers2["q4_1"], answers2["q4_2"]

st.write("")

all_answers = list(answers1.values()) + list(answers2.values())
done = sum(a is not None for a in all_answers)
total = len(all_answers)

st.markdown(f'<p class="progress-text">📝 진행률 — {done} / {total} 문항 완료</p>', unsafe_allow_html=True)
st.progress(done / total)

if done < total:
    st.button("🔒 모든 문항에 답하면 결과를 볼 수 있어요", use_container_width=True, disabled=True)
else:
    if st.button("🔍 결과 확인하기", use_container_width=True, type="primary"):
        st.balloons()
        dims = get_dimensions(price, service, location, vibe, q3_1, q3_2, q4_1, q4_2)
        code = "".join(d[0] for d in dims)
        name, desc, rec = TYPE_INFO[code]

        st.markdown(f"""
        <div class="result-card">
            <div class="code">{code}</div>
            <div class="name">{name}</div>
            <div class="desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

        st.info(f"💡 **이런 숙소가 잘 맞아요** — {rec}")

        st.markdown("### 📊 나의 성향 분포")
        st.markdown('<p class="q-desc">막대가 왼쪽으로 길수록 왼쪽 성향이에요. 숫자는 우세한 쪽의 비율이에요.</p>', unsafe_allow_html=True)
        for d_code, left_pct, l_label, r_label in dims:
            st.markdown(gauge_html(l_label, r_label, left_pct), unsafe_allow_html=True)
            if abs(left_pct - 50) < 10:
                st.caption(f"→ {l_label}·{r_label} 거의 반반! 상황 따라 양쪽 모습이 다 나와요.")

        st.markdown("### 🛏️ 컨디션 메모")
        st.markdown(f'<p class="q-desc">{comfort_note(sleep, hygiene)}</p>', unsafe_allow_html=True)