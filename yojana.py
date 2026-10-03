import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Yojana Setu", page_icon="⚖️", layout="centered")

# 2. Custom CSS Injection
st.markdown("""
<style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Professional Styling */
    .privacy-badge {
        background-color: #ecfeff;
        color: #0891b2;
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
        border: 1px solid #a5f3fc;
    }
    .main-title { font-size: 2.5rem; font-weight: 800; color: #0f172a; margin-bottom: 0; padding-bottom: 0; }
    .subtitle { font-size: 1.2rem; font-weight: 600; color: #334155; margin-top: 0; }
    .tagline { font-size: 1rem; color: #64748b; margin-bottom: 2rem; }
    .disclaimer { font-size: 0.8rem; color: #94a3b8; text-align: center; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #e2e8f0; }
    
    /* Scheme Cards */
    .scheme-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 8px;
        border-left: 6px solid #f97316;
        margin-bottom: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
    }
    .scheme-title { color: #0f172a; font-size: 1.25rem; font-weight: 700; margin-bottom: 8px; }
    .scheme-desc { color: #475569; font-size: 0.95rem; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# 3. The Professional Site Copy (Found in your inspect)
site_text = {
    "title": "Yojana Setu",
    "subtitle": "Government Scheme Finder & Application Guide",
    "tagline": "Discover what you qualify for in under 2 minutes — with zero identity compromise.",
    "privacyBadge": "Your answers stay on this device",
    "disclaimer": "Independent public service tool. Not an official Government of India website. Always verify details on official portals."
}

# 4. The Database
schemes_db = [
    {"id": 1, "title": "PM Kisan Samman Nidhi", "occupation": "farmer", "description": "Provides ₹6,000 per year to farmer families. Ensures direct benefit transfer to bank accounts."},
    {"id": 2, "title": "Post Matric Scholarship", "occupation": "student", "description": "Financial assistance for students pursuing higher education. Covers tuition and maintenance allowance."},
    {"id": 3, "title": "Mudra Yojana", "occupation": "business", "description": "Loans up to ₹10 Lakhs for small enterprises. No collateral required for micro-businesses."},
    {"id": 4, "title": "National Agricultural Market", "occupation": "farmer", "description": "Pan-India electronic trading portal networking existing APMC mandis."}
]

# 5. Build the UI Header
st.markdown(f'<div class="privacy-badge">🔒 {site_text["privacyBadge"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="main-title">{site_text["title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">{site_text["subtitle"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="tagline">{site_text["tagline"]}</div>', unsafe_allow_html=True)

# 6. The Questionnaire 
user_occupation = st.selectbox("What is your occupation?", ["Show All", "Farmer", "Student", "Business"])

st.write("---")
st.subheader("Eligible Schemes")

# 7. The Matchmaker Engine
eligible_schemes = [
    scheme for scheme in schemes_db 
    if scheme["occupation"] == user_occupation.lower() or user_occupation == "Show All"
]

if not eligible_schemes:
    st.info("No schemes found for this selection.")
else:
    for scheme in eligible_schemes:
        st.markdown(f"""
        <div class="scheme-card">
            <div class="scheme-title">{scheme['title']}</div>
            <div class="scheme-desc">{scheme['description']}</div>
        </div>
        """, unsafe_allow_html=True)

# 8. The Footer
st.markdown(f'<div class="disclaimer">{site_text["disclaimer"]}</div>', unsafe_allow_html=True)
