import streamlit as st
from datetime import datetime

# ==============================
# 페이지 설정
# ==============================
st.set_page_config(
    page_title="AI 심층활용도구",
    page_icon="rocket",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==============================
# CSS 디자인 (카드, 애니메이션, 반응형)
# ==============================
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stApp { max-width: 900px; margin: 0 auto; }
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin: 1rem 0;
        border-left: 5px solid #4361ee;
        transition: all 0.2s ease;
    }
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #4361ee;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .action-box {
        background: #e6f0ff;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4361ee;
        margin-top: 1rem;
        font-size: 0.95rem;
    }
    .fis-badge {
        background: #ff6b6b;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        display: inline-block;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ==============================
# 세션 상태 초기화
# ==============================
if 'logs' not in st.session_state:
    st.session_state.logs = []

# ==============================
# 콘텐츠 데이터 (이미지 포함)
# ==============================
content = {
    "A": {
        "title": "정보의 가치를 측정하고 골라주는 방법",
        "icon": "target",
        "color": "#4361ee",
        "fis": 9.2,
        "image_url": "https://images.unsplash.com/photo-1518432031352-d6fc5c10da5a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        "image_caption": "미래 충격 점수(FIS) – 시간 속 정보 가치의 흐름",
        "content": """
**미래 충격 점수 (FIS) 도입**  
> "이 뉴스는 미래에 얼마나 중요할까요?"  
AI가 **1년 뒤, 5년 뒤** 세상을 바꿀 가능성을 점수로 매김  
<span class="fis-badge">FIS: 9.2</span> 예: 작은 규제안 → 5년 후 산업 재편

**정보 투자 관리**  
> "당신의 생각은 한쪽으로 치우쳐 있지 않나요?"  
IT만 본다면? → 생물학, 정치학의 **숨겨진 연결고리** 추천

**미래 역추적 뉴스**  
> "2035년 기후 경제 붕괴" → 오늘의 **씨앗 3개** 역추적  
예: 작은 해양 플라스틱 규제 → 글로벌 공급망 재편

**시차 가치 분석**  
> "6개월 뒤 터질 뉴스"를 지금 저장 → 타임캡슐 알림
        """
    },
    "B": {
        "title": "뉴스레터의 내용과 구조 혁신",
        "icon": "lightbulb",
        "color": "#7209b7",
        "fis": 8.7,
        "image_url": "https://images.unsplash.com/photo-1516321310766-90c9cc76d8c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        "image_caption": "5단계 심층 해설 – 정보의 깊이 탐구 구조",
        "content": """
**5단계 심층 해설**  
1. 사실은?  
2. 왜 일어났나?  
3. 본질 원리는?  
4. 미래 영향은?  
5. **지금 내가 해야 할 행동?**

**How Might We?**  
> "이 정보를 우리 회사에 적용하면?"  
AI가 당신 직업 맞춤 질문 생성

**인과관계 지도**  
> 이 뉴스 ↔ 다른 산업 ↔ 정책 → **한눈에 시각화**

**노이즈-신호 분석**  
> 감정 70% 제거 → 핵심 신호만 추출
        """
    },
    "C": {
        "title": "정보 활용과 발전의 혁신",
        "icon": "rocket",
        "color": "#f72585",
        "fis": 9.5,
        "image_url": "https://images.unsplash.com/photo-1519389950474-36b3e4c9e7c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
        "image_caption": "AI와 딥다이브 토론 – 정보 → 행동 → 성장 사이클",
        "content": """
**반대편 관점 회전**  
> 환경 규제 찬성 vs "이 규제가 혁신을 죽인다"

**레버리지 포인트**  
> "최소 노력, 최대 효과" 적용 지점 제안

**정보-행동 로그**  
> 뉴스 → 회의 → 투자 → 결과 기록 → 학습

**AI와 딥다이브 토론**  
> "이 내용 더 깊이 물어보고 싶어요" → 실시간 대화
        """
    }
}

# ==============================
# 메인 타이틀
# ==============================
st.markdown("""
<div style="text-align:center; padding: 2rem 0;">
    <h1 style="color:#4361ee; margin:0;">AI 심층활용도구</h1>
    <p style="color:#666; font-size:1.1rem;">미래를 결정하는 정보, 지금 시작하세요</p>
</div>
""", unsafe_allow_html=True)

# ==============================
# 사이드바
# ==============================
with st.sidebar:
    st.header("사용자 설정")
    user_name = st.text_input("이름", value="미래 결정자")
    user_field = st.selectbox("관심 분야", 
        ["IT 기술", "생물학", "정치/경제", "기후/환경", "금융", "헬스케어"])
    
    st.markdown("---")
    st.markdown("### 최근 기록")
    if st.session_state.logs:
        for log in reversed(st.session_state.logs[-5:]):
            st.markdown(f"**{log['time']}**<br>{log['action'][:70]}...", unsafe_allow_html=True)
            st.markdown("---")
    else:
        st.caption("아직 기록 없음")

# ==============================
# 탭 생성
# ==============================
tab1, tab2, tab3 = st.tabs([
    "A. 정보 선별",
    "B. 구조 혁신", 
    "C. 활용 확장"
])

# ==============================
# 각 탭 렌더링 (use_container_width 사용!)
# ==============================
for tab, key in zip([tab1, tab2, tab3], ['A', 'B', 'C']):
    with tab:
        data = content[key]
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # 제목
        st.markdown(f"""
        <div class="section-title">
            <span style="font-size:1.5rem;">{data['icon']}</span> {data['title']}
        </div>
        """, unsafe_allow_html=True)
        
        # 이미지 (최신 파라미터 사용!)
        st.image(
            data['image_url'], 
            caption=data['image_caption'], 
            use_container_width=True  # 여기서 수정!
        )
        
        # FIS 뱃지
        st.markdown(f"<span class='fis-badge'>FIS: {data['fis']}/10</span>", unsafe_allow_html=True)
        
        # 본문
        st.markdown(data['content'])
        
        # 활용 질문
        with st.expander("이 정보, 어떻게 활용할까? (How Might We?)", expanded=False):
            action = st.text_area(
                f"{key} 섹션에서 얻은 아이디어 또는 행동 계획",
                placeholder="예: FIS 개념을 팀 회의에 도입해 뉴스 필터링 시작",
                height=100,
                key=f"input_{key}"
            )
            
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("기록 저장", key=f"save_{key}"):
                    if action.strip():
                        st.session_state.logs.append({
                            "section": key,
                            "action": action,
                            "time": datetime.now().strftime("%m/%d %H:%M")
                        })
                        st.success("기록 완료!")
                        st.balloons()
                    else:
                        st.warning("내용을 입력해주세요.")
            with col2:
                st.caption(f"예상 영향도: **{data['fis']}/10** | 추천 우선순위: 높음")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# 푸터
# ==============================
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#888; font-size:0.9rem; padding:1rem;">
    <strong>AI 심층활용도구 v1.1</strong> | 
    미래는 정보에서 시작됩니다<br>
    <em>Powered by Streamlit</em>
</div>
""", unsafe_allow_html=True)
