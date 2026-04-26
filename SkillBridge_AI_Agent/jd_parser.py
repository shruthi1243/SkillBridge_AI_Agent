import re

TECH_SKILLS = [
    "Python", "Java", "SQL", "Machine Learning", "Deep Learning",
    "Data Structures", "HTML", "CSS", "JavaScript", "APIs",
    "Cloud", "AWS", "Azure", "Communication", "Problem Solving",
    "Git", "GitHub", "OOP", "DBMS"
]

def extract_jd_skills(job_description):
    found_skills = []
    for skill in TECH_SKILLS:
        if re.search(skill, job_description, re.IGNORECASE):
            found_skills.append(skill)
    return found_skills