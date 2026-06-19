import streamlit as st

st.set_page_config(page_title="여행 숙소 성향 테스트", page_icon="🧳", layout="centered")

st.markdown("""
<style>
.stApp { background: #f6f5fb; }

.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 4rem;
    font-size: 16px;
}

.section-head { margin: 8px 0 4px 0; }
.section-head h2 { font-size: 25px; font-weight: 800; color: #2d2b45; margin: 0 0 6px 0; }
.section-head p  { font-size: 15px; line-height: 1.7; color: #8a879c; margin: 0; }

/* 라디오 (PART 1) */
div[role="radiogroup"] {
    gap: 14px;
    justify-content: center;
    padding: 6px 0 2px 0;
    flex-wrap: wrap;
}
div[role="radiogroup"] label {
    font-size: 14px !important;
    font-weight: 600;
    color: #5a5870;
    transition: transform 0.15s ease, color 0.15s ease;
}
div[role="radiogroup"] label:hover { transform: scale(1.10); color: #6c5ce7; }
div[role="radiogroup"] label p { font-size: 14px !important; }

/* 슬라이더 (PART 2) 보라 테마 */
div[data-testid="stSlider"] [role="slider"] {
    background-color: #6c5ce7 !important;
    box-shadow: 0 0 0 0.2rem rgba(108, 92, 231, 0.18) !important;
}
div[data-testid="stSlider"] [data-baseweb="slider"] > div > div {
    background: #6c5ce7 !important;
}
div[data-testid="stSlider"] [data-testid="stTickBarMin"],
div[data-testid="stSlider"] [data-testid="stTickBarMax"] { color: #8a879c; }

/* 질문 카드 */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff;
    border: 1px solid #ecebf5 !important;
    border-radius: 16px;
    padding: 20px 26px !important;
    margin-bottom: 18px;
    box-shadow: 0 2px 10px rgba(90, 80, 160, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 26px rgba(108, 92, 231, 0.13);
}

.q-title { font-size: 20px !important; font-weight: 700; color: #2d2b45; margin: 2px 0 8px 0; }
.q-desc  { font-size: 15px !important; line-height: 1.75; color: #6e6c80; margin-bottom: 14px; }

/* PART 2 양극단 */
.anchor-wrap { display: flex; gap: 14px; margin: 4px 0 10px 0; }
.anchor {
    flex: 1; padding: 14px 16px; border-radius: 12px;
    font-size: 14px !important; line-height: 1.6;
}
.anchor.low  { background: #eef0ff; color: #4a56c4; }
.anchor.high { background: #f7eefc; color: #9242b8; text-align: right; }

/* 배너 */
.banner {
    background: linear-gradient(270deg, #6c5ce7, #8e7cf0, #a29bfe, #7d6cf0);
    background-size: 600% 600%;
    animation: gradientShift 11s ease infinite;
    border-radius: 22px;
    padding: 46px 34px;
    text-align: center;
    color: white;
    margin-bottom: 22px;
    box-shadow: 0 12px 34px rgba(108, 92, 231, 0.28);
}
.banner .emoji { font-size: 40px; display: block; margin-bottom: 6px; }
.banner h1 { color: white; font-size: 34px; font-weight: 800; margin: 0 0 10px 0; letter-spacing: -0.5px; }
.banner p  { color: #ece9ff; font-size: 16px; line-height: 1.6; margin: 0; }
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* 결과 카드 */
.result-card {
    background: linear-gradient(135deg, #6c5ce7 0%, #9242b8 100%);
    border-radius: 22px;
    padding: 42px 32px;
    text-align: center;
    color: white;
    margin: 18px 0;
    box-shadow: 0 14px 36px rgba(108, 92, 231, 0.30);
    animation: popIn 0.6s cubic-bezier(0.18, 0.89, 0.32, 1.28);
}
.result-card .code { font-size: 16px; letter-spacing: 7px; opacity: 0.8; }
.result-card .name { font-size: 38px; font-weight: 800; margin: 10px 0; letter-spacing: -0.5px; }
.result-card .desc { font-size: 17px; line-height: 1.8; color: #f1eeff; max-width: 600px; margin: 0 auto; }
@keyframes popIn {
    0%   { opacity: 0; transform: scale(0.85) translateY(22px); }
    100% { opacity: 1; transform: scale(1)    translateY(0); }
}

/* 중앙 기준 양방향 게이지 */
.bi-row {
    display: grid;
    grid-template-columns: 150px 1fr 150px;
    align-items: center;
    gap: 12px;
    margin: 18px 0;
}
.bi-label { font-size: 14px; font-weight: 700; color: #b9b7ca; }
.bi-label.left  { text-align: right; }
.bi-label.right { text-align: left; }
.bi-label.strong { color: #6c5ce7; }
.bi-pct { font-size: 12px; font-weight: 700; opacity: 0.85; }

.bi-track { position: relative; display: flex; height: 22px; }
.bi-track::before {
    content: ""; position: absolute; left: 50%; top: -4px; bottom: -4px;
    width: 2px; transform: translateX(-50%);
    background: #cbc7de; border-radius: 1px; z-index: 3;
}
.bi-balance {
    position: absolute; left: 50%; top: 50%;
    transform: translate(-50%, -50%);
    z-index: 4;
    background: #ffffff;
    color: #8a879c;
    font-size: 11px; font-weight: 800;
    padding: 2px 10px; border-radius: 999px;
    border: 1.5px solid #cbc7de;
    white-space: nowrap;
}
.bi-half {
    flex: 1; height: 100%; display: flex; overflow: hidden;
    background: #ebe8f5;
}
.bi-half.left  { justify-content: flex-end;   border-radius: 11px 0 0 11px; }
.bi-half.right { justify-content: flex-start;  border-radius: 0 11px 11px 0; }
.bi-fill {
    height: 100%;
    background: linear-gradient(90deg, #6c5ce7, #9242b8);
    animation: fillUp 1.0s ease-out;
}
@keyframes fillUp { from { width: 0 !important; } }

.result-head { font-size: 21px; font-weight: 800; color: #2d2b45; margin: 26px 0 8px 0; }
.progress-text { font-size: 15px; font-weight: 700; color: #6c5ce7; margin-bottom: 4px; }
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

LABELS_P1 = ["전혀 중요하지 않음", "별로 중요하지 않음", "보통임", "중요함", "매우 중요함"]
SLIDER_OPTS = ["①", "②", "③", "④", "⑤"]

def lean(a, b):
    """두 중요도 점수의 '차이'로 왼쪽(a) 기울기 % 계산 (일관적·선형)."""
    return 50 + (a - b) / 4 * 50

def slider_lean(avg):
    """슬라이더 평균(1~5)을 그대로 왼쪽 기울기 %로 변환."""
    return (avg - 1) / 4 * 100

def get_dimensions(price, service, location, vibe, q3_1, q3_2, q4_1, q4_2):
    dims = []
    pe = lean(price, service)
    dims.append(("E" if pe >= 50 else "P", pe, "💰 가성비", "✨ 프리미엄"))
    pl = lean(location, vibe)
    dims.append(("L" if pl >= 50 else "V", pl, "📍 효율", "🌿 감성"))
    pr = slider_lean((q3_1 + q3_2) / 2)
    dims.append(("R" if pr >= 50 else "A", pr, "🛋️ 휴식", "🏃 액티브"))
    pc = slider_lean((q4_1 + q4_2) / 2)
    dims.append(("C" if pc >= 50 else "S", pc, "🗓️ 계획", "🎲 즉흥"))
    return dims

def gauge_html(left_label, right_label, left_pct):
    dev = left_pct - 50
    left_fill = max(dev, 0) / 50 * 100
    right_fill = max(-dev, 0) / 50 * 100
    dom_pct = max(left_pct, 100 - left_pct)
    is_balanced = (dev == 0)

    left_cls = "strong" if dev > 0 else ""
    right_cls = "strong" if dev < 0 else ""
    left_txt = f'{left_label} <span class="bi-pct">{dom_pct:.0f}%</span>' if dev > 0 else left_label
    right_txt = f'{right_label} <span class="bi-pct">{dom_pct:.0f}%</span>' if dev < 0 else right_label

    badge = '<span class="bi-balance">균형</span>' if is_balanced else ''

    return (
        f'<div class="bi-row">'
        f'<div class="bi-label left {left_cls}">{left_txt}</div>'
        f'<div class="bi-track">'
        f'<div class="bi-half left"><div class="bi-fill" style="width:{left_fill:.0f}%"></div></div>'
        f'<div class="bi-half right"><div class="bi-fill" style="width:{right_fill:.0f}%"></div></div>'
        f'{badge}'
        f'</div>'
        f'<div class="bi-label right {right_cls}">{right_txt}</div>'
        f'</div>'
    )

def comfort_note(sleep, hygiene):
    notes = []
    if sleep >= 4:
        notes.append("잠자리가 편해야 여행이 즐겁다고 느끼는 편이네요.<br>침구 상태나 방음 후기를 꼭 확인해 보세요.")
    elif sleep <= 2:
        notes.append("잠자리에 크게 예민하지 않은 편이라<br>고를 수 있는 숙소의 폭이 넓어요.")
    if hygiene >= 4:
        notes.append("위생은 절대 양보할 수 없는 조건이네요.<br>청결 평점이 높은 숙소 위주로 살펴보세요.")
    elif hygiene <= 2:
        notes.append("위생은 어느 정도 감수하는 편이라<br>개성 있는 숙소도 부담 없이 도전해 볼 수 있어요.")
    if not notes:
        notes.append("수면도 위생도 무난하게 보는 편이라<br>전반적으로 균형 잡힌 선택을 하게 될 것 같아요.")
    return "<br><br>".join(notes)

def mark_touched(k):
    st.session_state[f"touched_{k}"] = True

def reset_test():
    for k in list(st.session_state.keys()):
        del st.session_state[k]

# ── 헤더 ──
st.markdown("""
<div class="banner">
    <span class="emoji">🧳</span>
    <h1>여행 숙소 성향 테스트</h1>
    <p>10개의 질문으로 알아보는 나의 여행 유형<br>당신은 16가지 유형 중 어디에 해당하나요?</p>
</div>
""", unsafe_allow_html=True)

# ── PART 1 ──
st.markdown('<div class="section-head"><h2>PART 1 · 숙소 선택 기준</h2><p>숙소를 고를 때 아래 항목이 얼마나 중요한지 골라주세요.</p></div>', unsafe_allow_html=True)

questions_part1 = [
    ("💸 가격",
     "숙소를 고를 때 가격을 얼마나 따지는 편인가요?<br>"
     "비슷한 조건이면 조금이라도 더 저렴한 곳을 찾게 되나요?"),
    ("🛎️ 서비스",
     "직원의 친절함이나 룸서비스, 조식 같은 서비스가 얼마나 중요한가요?<br>"
     "누군가 살뜰히 챙겨주는 느낌이 만족도를 좌우하나요?"),
    ("📍 위치",
     "위치가 숙소 선택에 얼마나 큰 영향을 주나요?<br>"
     "역이나 관광지에서 가까운 게 우선인가요?"),
    ("✨ 분위기",
     "숙소의 분위기를 얼마나 중요하게 보나요?<br>"
     "인테리어나 뷰처럼 공간이 주는 감성에 끌리는 편인가요?"),
    ("😴 수면의 질",
     "잘 자는 환경을 얼마나 따지나요?<br>"
     "침구가 편하고 조용해야 다음 날 컨디션이 좋은 편인가요?"),
    ("🧼 위생",
     "청결함이 숙소 선택에서 얼마나 중요한가요?<br>"
     "조금이라도 더러우면 마음이 불편한 편인가요?"),
]

answers1 = {}
for title, desc in questions_part1:
    with st.container(border=True):
        st.markdown(f'<p class="q-title">{title}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="q-desc">{desc}</p>', unsafe_allow_html=True)
        answers1[title] = st.radio(title, LABELS_P1, index=None, horizontal=True,
                                   label_visibility="collapsed", key=f"r1_{title}")

st.write("")

# ── PART 2 ──
st.markdown('<div class="section-head"><h2>PART 2 · 여행 스타일</h2><p>정답은 없어요. 양쪽 설명을 보고 나와 가까운 쪽으로 슬라이더를 드래그해 주세요.</p></div>', unsafe_allow_html=True)

questions_part2 = [
    ("q3_1", "🛋️ 나에게 숙소란?",
     "잠만 잘 수 있으면 충분해요.<br>여행은 밖에서 즐기는 거니까요.",
     "여행의 핵심 공간이에요.<br>좋은 방에서 오래 머물고 싶어요."),
    ("q3_2", "🛌 여행 중에 쉬는 시간이 필요한가요?",
     "쉴 틈 없이 알차게 채우는 게 좋아요.<br>쉬면 오히려 시간이 아까워요.",
     "푹 쉬는 시간이 꼭 있어야 해요.<br>그래야 진짜 여행한 기분이 들어요."),
    ("q4_1", "🗓️ 여행 계획은 어떻게 짜나요?",
     "현지에서 그때그때 정하는 편이에요.<br>빡빡한 계획은 답답해요.",
     "출발 전에 거의 다 정해둬요.<br>준비가 돼 있어야 마음이 편해요."),
    ("q4_2", "🎲 갑자기 변수가 생기면?",
     "그것도 여행의 재미라고 생각해요.<br>즉흥적으로 대처하는 게 즐거워요.",
     "계획이 틀어지면 좀 불편해요.<br>변수는 미리 줄여두고 싶어요."),
]

answers2 = {}
for key, title, low, high in questions_part2:
    with st.container(border=True):
        st.markdown(f'<p class="q-title">{title}</p>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="anchor-wrap">'
            f'<div class="anchor low">◀ {low}</div>'
            f'<div class="anchor high">{high} ▶</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        answers2[key] = st.select_slider(
            key, options=SLIDER_OPTS, value="③",
            key=key, on_change=mark_touched, args=(key,),
            label_visibility="collapsed",
        )

st.write("")

# ── 진행률 ──
p2_keys = [q[0] for q in questions_part2]
done_p1 = sum(a is not None for a in answers1.values())
done_p2 = sum(st.session_state.get(f"touched_{k}", False) for k in p2_keys)
done = done_p1 + done_p2
total = len(answers1) + len(p2_keys)

st.markdown(f'<p class="progress-text">📝 진행률 — {done} / {total} 문항 완료</p>', unsafe_allow_html=True)
st.progress(done / total)

# ── 결과 제출 ──
if done < total:
    st.button("🔒 모든 문항에 답하면 결과를 볼 수 있어요", use_container_width=True, disabled=True)
else:
    if st.button("🔍 결과 확인하기", use_container_width=True, type="primary"):
        st.session_state["submitted"] = True
        st.balloons()

# ── 결과 표시 (제출 후 유지) ──
if st.session_state.get("submitted") and done == total:
    s1 = {k: LABELS_P1.index(v) + 1 for k, v in answers1.items()}
    price, service = s1["💸 가격"], s1["🛎️ 서비스"]
    location, vibe = s1["📍 위치"], s1["✨ 분위기"]
    sleep, hygiene = s1["😴 수면의 질"], s1["🧼 위생"]

    s2 = {k: SLIDER_OPTS.index(answers2[k]) + 1 for k in p2_keys}
    q3_1, q3_2 = s2["q3_1"], s2["q3_2"]
    q4_1, q4_2 = s2["q4_1"], s2["q4_2"]

    dims = get_dimensions(price, service, location, vibe, q3_1, q3_2, q4_1, q4_2)
    code = "".join(d[0] for d in dims)
    name, desc, rec = TYPE_INFO[code]

    st.markdown(
        f'<div class="result-card">'
        f'<div class="code">{code}</div>'
        f'<div class="name">{name}</div>'
        f'<div class="desc">{desc}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.info(f"💡 **이런 숙소가 잘 맞아요** — {rec}")

    st.markdown('<p class="result-head">📊 나의 성향 분포</p>', unsafe_allow_html=True)
    for d_code, left_pct, l_label, r_label in dims:
        st.markdown(gauge_html(l_label, r_label, left_pct), unsafe_allow_html=True)

    st.markdown('<p class="result-head">🛏️ 컨디션 메모</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="q-desc">{comfort_note(sleep, hygiene)}</p>', unsafe_allow_html=True)

    st.write("")
    st.button("🔄 다시 검사하기", use_container_width=True, on_click=reset_test)
