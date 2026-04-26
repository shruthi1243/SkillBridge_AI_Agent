import streamlit as st
import pandas as pd
import plotly.express as px

from resume_parser import extract_resume_text
from jd_parser import extract_jd_skills
from assessment_engine import generate_assessment_questions
from scoring_engine import match_resume_with_skills, calculate_scores, identify_skill_gaps
from learning_plan import generate_learning_plan

st.set_page_config(page_title="SkillBridge AI Agent", layout="wide")

st.title("🤖 SkillBridge AI - Skill Assessment & Personalized Learning Agent")
st.write("An AI Agent that compares Job Requirements with Candidate Resume, conversationally assesses proficiency, identifies gaps and creates a personalized upskilling roadmap.")

job_description = st.text_area("📋 Paste Job Description Here")
uploaded_resume = st.file_uploader("📄 Upload Candidate Resume (PDF)", type=["pdf"])

if "questions_generated" not in st.session_state:
    st.session_state.questions_generated = False

if "required_skills" not in st.session_state:
    st.session_state.required_skills = []

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if job_description and uploaded_resume:
    if st.button("🚀 Generate AI Assessment Questions"):
        st.session_state.resume_text = extract_resume_text(uploaded_resume)
        st.session_state.required_skills = extract_jd_skills(job_description)
        st.session_state.questions_generated = True

if st.session_state.questions_generated:

    required_skills = st.session_state.required_skills
    resume_text = st.session_state.resume_text

    st.subheader("📌 Skills Extracted From Job Description")
    st.write(required_skills)

    assessment_questions = generate_assessment_questions(required_skills)

    st.subheader("🧠 AI Conversational Skill Assessment")

    with st.form("candidate_assessment_form"):
        candidate_answers = {}

        for skill, question in assessment_questions:
            st.write(f"**{skill}:** {question}")
            candidate_answers[skill] = st.text_area(f"Enter candidate answer for {skill}", key=skill)

        submit_eval = st.form_submit_button("✅ Evaluate Candidate")

    if submit_eval:

        matched_skills = match_resume_with_skills(resume_text, required_skills)

        st.subheader("📄 Resume Skill Matching Analysis")
        for skill, status in matched_skills.items():
            if status:
                st.write(f"✅ {skill} mentioned in resume")
            else:
                st.write(f"❌ {skill} not clearly mentioned in resume")

        scores = calculate_scores(required_skills, matched_skills, candidate_answers)

        st.subheader("📊 Candidate Proficiency Scores")
        df = pd.DataFrame(list(scores.items()), columns=["Skill", "Score"])
        st.dataframe(df)

        fig = px.bar(df, x="Skill", y="Score", title="Skill Proficiency Analysis")
        st.plotly_chart(fig)

        skill_gaps = identify_skill_gaps(required_skills, scores)

        st.subheader("⚠️ Identified Skill Gaps")
        st.write(skill_gaps if skill_gaps else "No Major Skill Gaps")

        roadmap = generate_learning_plan(skill_gaps)

        st.subheader("📚 Personalized Learning Roadmap")
        for week, task in roadmap.items():
            st.write(f"**{week}:** {task}")