import streamlit as st

# 1. Page Configuration (Hides default menus and sets title)
st.set_page_config(page_title="Yojana Setu Clone", page_icon="🏛️", layout="centered")

# 2. Custom CSS Injection (This makes it look professional)
st.markdown("""
<style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Make the dropdown question bolder */
    .stSelectbox label {font-size: 1.1rem; font-weight: 600;}
    
    /* Create custom professional cards for the schemes */
    .scheme-card {
        background-color: #1e293b;
        padding: 24px;
        border-radius: 8px;
        border-left: 6px solid #10b981; /* Green accent line */
        margin-bottom: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .scheme-title {
        color: #f8fafc; 
        font-size: 1.4rem; 
        font-weight: 700; 
        margin-bottom: 8px;
    }
    .scheme-desc {
        color: #94a3b8; 
        font-size: 1rem;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)

# 3. The Data
schemes_db = [
    {"id": 1, "title": "PM Kisan Samman Nidhi", "occupation": "farmer", "description": "Provides ₹6,000 per year to farmer families. Ensures direct benefit transfer to bank accounts."},
    {"id": 2, "title": "Post Matric Scholarship", "occupation": "student", "description": "Financial assistance for students pursuing higher education. Covers tuition and maintenance allowance."},
    {"id": 3, "title": "Mudra Yojana", "occupation": "business", "description": "Loans up to ₹10 Lakhs for small enterprises. No collateral required for micro-businesses."},
    {"id": 4, "title": "National Agricultural Market", "occupation": "farmer", "description": "Pan-India electronic trading portal networking existing APMC mandis."}
]

# 4. The Interface
st.title("🏛️ Scheme Finder")
st.markdown("Answer basic questions to see your eligible government schemes.")
st.write("---")

user_occupation = st.selectbox("What is your occupation?", ["Show All", "farmer", "student", "business"])

# 5. The Matchmaker (Filtering)
st.subheader("Results")

eligible_schemes = [
    scheme for scheme in schemes_db 
    if scheme["occupation"] == user_occupation.lower() or user_occupation == "Show All"
]

# Display the results using our custom CSS cards
if not eligible_schemes:
    st.info("No schemes found for this selection.")
else:
    for scheme in eligible_schemes:
        # Instead of default Streamlit success boxes, we use our custom HTML cards
        st.markdown(f"""
        <div class="scheme-card">
            <div class="scheme-title">{scheme['title']}</div>
            <div class="scheme-desc">{scheme['description']}</div>
        </div>
        """, unsafe_allow_html=True)
