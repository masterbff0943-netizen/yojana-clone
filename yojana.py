import streamlit as st

# 1. The Data
schemes_db = [
    {"id": 1, "title": "PM Kisan Samman Nidhi", "occupation": "farmer", "description": "Provides ₹6,000 per year to farmer families."},
    {"id": 2, "title": "Post Matric Scholarship", "occupation": "student", "description": "Financial assistance for students pursuing higher education."},
    {"id": 3, "title": "Mudra Yojana", "occupation": "business", "description": "Loans up to ₹10 Lakhs for small enterprises."},
    {"id": 4, "title": "National Agricultural Market", "occupation": "farmer", "description": "Pan-India electronic trading portal."}
]

# 2. The Interface
st.title("My Scheme Finder")
user_occupation = st.selectbox("What is your occupation?", ["all", "farmer", "student", "business"])

# 3. The Matchmaker (Filtering)
st.subheader(f"Schemes for: {user_occupation.upper()}")

eligible_schemes = [
    scheme for scheme in schemes_db 
    if scheme["occupation"] == user_occupation or user_occupation == "all"
]

# Display the results
if not eligible_schemes:
    st.warning("No schemes found for this occupation.")
else:
    for scheme in eligible_schemes:
        with st.container():
            st.success(f"**{scheme['title']}**")
            st.write(scheme['description'])
