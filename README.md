🤖 SkillBridge AI Agent
AI-Powered Skill Assessment & Personalized Learning Plan Agent

SkillBridge AI Agent is an intelligent recruitment assistance platform developed for the Deccan AI Hackathon. Traditional resumes only show what a candidate claims to know, but they fail to measure real-world proficiency.
This AI Agent bridges that gap by comparing a Job Description with a Candidate Resume, conducting a conversational skill assessment, identifying skill deficiencies, and generating a personalized upskilling roadmap.

 📄 Problem Statement
->SkillBridge AI solves this by:
-> Extracting required skills from Job Descriptions
-> Parsing candidate resumes automatically
->Generating AI-based technical assessment questions
->Evaluating candidate proficiency based on resume match + responses
-> Detecting skill gaps
-> Creating a personalized weekly learning plan

📋 Core Features:
Job Description Skill Extraction
Resume Parsing using PDF Reader
AI Conversational Technical Assessment
Candidate Skill Proficiency Scoring Dashboard
Skill Gap Identification
Personalized Weekly Learning Roadmap
Visual Skill Analysis using Interactive Charts

🛠️ Tech stack used:
- Python 3.12
- Streamlit
- PyPDF2
- Pandas
- Plotly
- Rule-Based NLP Matching
- VS Code
- GitHub
  
📚 Project Architecture:
-User uploads Candidate Resume
- User pastes Job Description
- System extracts required technical skills
- AI generates technical interview questions
- Candidate answers are evaluated
- Resume skill matching is performed
- Skill proficiency scores are calculated
-Skill gaps are identified
- Personalized learning roadmap is generated

📂 Project Files:
- `app.py` → Main Streamlit Application
- `resume_parser.py` → Resume PDF Text Extraction
- `jd_parser.py` → Job Description Skill Extraction
- `assessment_engine.py` → AI Question Generation
- `scoring_engine.py` → Resume Matching + Candidate Scoring
- `learning_plan.py` → Personalized Learning Plan Generator

How to Run Locally:
```bash
pip install -r requirements.txt
streamlit run app.py

🎯 Innovation
SkillBridge AI combines resume matching, conversational answer evaluation, technical scoring, and roadmap recommendation to provide a realistic AI-powered hiring assistant.

👩‍💻 Developed By
Shruthi Biradar
