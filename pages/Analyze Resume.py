import streamlit as st
from module.resume_parser import extract_text_from_pdf, extract_skills
from module.gap_analyzer import evaluate_resume
from module.load_dataset import load_skill_database
from module.gpt_feedback import resume_feedback
from module.pdf_generator import generate_pdf
import pandas as pd

st.set_page_config(page_title="CareerLens", layout="wide")
import streamlit as st

# Set full-page background image

st.title("📄 RoleFit Analyzer")

# Upload section
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# Role selection
skills_df = pd.read_csv("data/skills_data.csv")
roles = skills_df['Role'].unique() 
roles = ["-- Select Job role --"] + list(roles)
selected_role = st.selectbox("Select a job role you’re targeting:", roles)

# Submit
if uploaded_file and selected_role != "-- Select Job role --":

    st.subheader("🔍:green[ Analyzing Resume...]")

    resume_text = extract_text_from_pdf(uploaded_file)
    role_skills = load_skill_database("data/skills_data.csv",selected_role)
    resume_skills = extract_skills(resume_text,role_skills)
    report = evaluate_resume(resume_skills, role_skills,selected_role)
    feedback = resume_feedback(resume_text, role_skills, selected_role)

    st.markdown("##### ✅ Skill Match Score")
    st.progress(report['Score'] / 10)
    if report['Matched Keywords']:
        for keyword in report['Matched Keywords']:
            st.markdown(f"**Matched Skills:** `{keyword}`")
    else:
        st.markdown(f"**Matched Skills:**  `🔍 No relevant skills found` ")

    
    st.markdown("#### Feedback")
    with st.chat_message("ai"):
        for line in feedback:
            if line:
                if '+' in line:
                    st.markdown("&emsp;&emsp;->" + line.replace('+',''))
                else:
                    st.markdown(line)
            else:
                st.markdown(" ")
         
    pdf_bytes = generate_pdf(feedback)
    st.download_button("📥 Download Feedback",data = pdf_bytes, file_name="career_feedback.pdf",mime="application/pdf")