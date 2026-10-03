import streamlit as st

# 1. Page Configuration (Set to Wide to mimic a real web app)
st.set_page_config(page_title="Yojana Setu", page_icon="⚖️", layout="wide")

# 2. Advanced Dark Mode CSS Injection
st.markdown("""
<style>
    /* Force Dark Backgrounds and Hide Streamlit UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #0f172a; } /* Slate 900 */
    
    /* Header Typography */
    .main-title { font-size: 2.2rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.5rem; }
    .subtitle { font-size: 1rem; color: #94a3b8; margin-bottom: 2rem; }
    
    /* Complex Dark Mode Scheme Cards */
    .scheme-card {
        background-color: #1e293b; /* Slate 800 */
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px solid #334155;
        transition: transform 0.2s;
    }
    .scheme-card:hover { border-color: #475569; }
    
    /* Badges row */
    .badge-row { display: flex; gap: 12px; margin-bottom: 16px; align-items: center; }
    .badge-status { background-color: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 6px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
    .badge-pillar { background-color: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 4px 12px; border-radius: 6px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
    
    /* Content */
    .scheme-title { color: #f8fafc; font-size: 1.4rem; font-weight: 600; margin-bottom: 12px; }
    .scheme-desc { color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px; }
    .scheme-benefit { color: #94a3b8; font-size: 0.9rem; padding-left: 12px; border-left: 3px solid #3b82f6; margin-bottom: 16px; }
    
    /* Footer row with Relevance Score */
    .card-footer { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #334155; padding-top: 16px; }
    .relevance { font-size: 0.85rem; color: #94a3b8; font-weight: 500; }
    .score-num { color: #f8fafc; font-weight: 700; font-size: 1rem; }
    .details-btn { color: #38bdf8; font-size: 0.9rem; font-weight: 600; cursor: pointer; }
</style>
""", unsafe_allow_html=True)

# 3. The Upgraded Database (Mimicking the real site's data structure)
schemes_db = [
    {
        "id": 1, 
        "title": "Post-Matric Scholarship for SC Students", 
        "occupation": "student",
        "pillar": "LIBERTY",
        "status": "Possibly Eligible",
        "score": "73",
        "description": "Financial assistance to Scheduled Caste students studying at post-matriculation or post-secondary stage.",
        "benefit": "100% compulsory non-refundable college fees reimbursement plus monthly maintenance allowance directly credited via DBT."
    },
    {
        "id": 2, 
        "title": "Atal Pension Yojana (APY)", 
        "occupation": "all",
        "pillar": "FRATERNITY",
        "status": "Possibly Eligible",
        "score": "60",
        "description": "Government-backed guaranteed pension scheme for unorganised sector workers between 18 and 40 years.",
        "benefit": "Guaranteed minimum monthly pension of ₹1,000, ₹2,000, ₹3,000, ₹4,000 or ₹5,000 from age 60 until lifetime."
    }
]

# 4. Layout using Streamlit Columns (To mimic the sidebar structure)
col1, col2 = st.columns([1, 2.5])

with col1:
    st.markdown('<div class="main-title">Yojana Setu</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Government Scheme Finder & Application Guide<br>Discover what you qualify for in under 2 minutes.</div>', unsafe_allow_html=True)
    st.write("---")
    user_occupation = st.selectbox("Your Occupation:", ["all", "student", "business", "farmer"])
    st.info("💡 Answer more questions to unlock targeted schemes.")

with col2:
    # 5. The Matchmaker Engine
    eligible_schemes = [
        scheme for scheme in schemes_db 
        if scheme["occupation"] == user_occupation.lower() or scheme["occupation"] == "all"
    ]

    st.markdown(f"<h3 style='color: #f8fafc; margin-bottom: 20px;'>{len(eligible_schemes)} Schemes Found</h3>", unsafe_allow_html=True)

    # 6. Render the Complex Cards
    for scheme in eligible_schemes:
        st.markdown(f"""
        <div class="scheme-card">
            <div class="badge-row">
                <span class="badge-status">{scheme['status']}</span>
                <span class="badge-pillar">{scheme['pillar']}</span>
            </div>
            <div class="scheme-title">{scheme['title']}</div>
            <div class="scheme-desc">{scheme['description']}</div>
            <div class="scheme-benefit"><b>Benefit:</b> {scheme['benefit']}</div>
            <div class="card-footer">
                <div class="relevance">Relevance: <span class="score-num">{scheme['score']}</span>/100</div>
                <div class="details-btn">Details →</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
