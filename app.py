import streamlit as st
import pandas as pd
from utils.recommend import recommend_career

# Load mapping file
data = pd.read_csv("data/career_mapping.csv")

st.set_page_config(page_title="Career Path Recommender", layout="centered")
st.title("🎯 AI Career Path Recommender")
st.markdown("Fill in your details and we'll recommend a suitable career path!")

# Collect user input
name = st.text_input("Full Name")
age = st.slider("Age", 16, 40)
education = st.selectbox("Education Level", ["High School", "Undergraduate", "Graduate", "Postgraduate"])
interests = st.multiselect("Select Your Interests", ["Data", "Design", "Business", "Engineering", "Marketing", "Healthcare"])
skills = st.multiselect("Your Current Skills", ["Python", "Excel", "Communication", "SQL", "Graphic Design", "Public Speaking"])

if st.button("🔍 Recommend Career Path"):
    if not interests or not skills:
        st.warning("Please select at least one interest and one skill.")
    else:
        recommendations = recommend_career(interests, skills, data)
        st.success(f"Hi {name}, based on your profile, here are your recommended paths:")
        for rec in recommendations:
            st.subheader(rec['career'])
            st.markdown(f"**Step 1**: {rec['step1']}")
            st.markdown(f"**Step 2**: {rec['step2']}")
            st.markdown(f"**Step 3**: {rec['step3']}")
