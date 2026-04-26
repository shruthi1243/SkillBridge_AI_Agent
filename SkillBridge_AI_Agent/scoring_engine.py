import random

def match_resume_with_skills(resume_text, required_skills):
    matched = {}
    resume_lower = resume_text.lower()

    synonyms = {
        "SQL": ["sql", "structured query language", "mysql", "postgresql"],
        "Machine Learning": ["machine learning", "ml", "model training"],
        "Git": ["git", "version control"],
        "GitHub": ["github", "repository"],
        "APIs": ["api", "rest api", "backend integration"],
        "DBMS": ["dbms", "database management", "database"],
        "Communication": ["communication", "teamwork", "presentation"],
        "Problem Solving": ["problem solving", "debugging", "analytical"],
        "Cloud": ["cloud", "aws", "azure", "gcp"]
    }

    for skill in required_skills:
        found = False

        if skill.lower() in resume_lower:
            found = True
        elif skill in synonyms:
            for word in synonyms[skill]:
                if word in resume_lower:
                    found = True

        matched[skill] = found

    return matched


def calculate_scores(required_skills, matched_skills, candidate_answers):
    scores = {}
    for skill in required_skills:
        base = 0

        if matched_skills[skill]:
            base += random.randint(4, 5)
        else:
            base += random.randint(2, 3)

        if len(candidate_answers.get(skill, "")) > 20:
            base += random.randint(2, 4)
        else:
            base += random.randint(1, 2)

        scores[skill] = min(base, 10)

    return scores


def identify_skill_gaps(required_skills, scores):
    gaps = []
    for skill in required_skills:
        if scores.get(skill, 0) < 6:
            gaps.append(skill)
    return gaps