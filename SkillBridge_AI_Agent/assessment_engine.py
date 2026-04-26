def generate_assessment_questions(skills):
    question_bank = {
        "Python": "Explain list comprehension in Python with an example.",
        "Java": "What is inheritance in Java?",
        "SQL": "What is the difference between WHERE and HAVING clause?",
        "Machine Learning": "Explain supervised vs unsupervised learning.",
        "Deep Learning": "What is the purpose of activation functions?",
        "Data Structures": "Explain stack and queue.",
        "HTML": "What are semantic tags in HTML?",
        "CSS": "Difference between flexbox and grid?",
        "JavaScript": "What is closure in JavaScript?",
        "APIs": "What is REST API?",
        "Cloud": "What is cloud computing?",
        "AWS": "What is EC2 in AWS?",
        "Azure": "What is Azure Blob Storage?",
        "Communication": "How do you explain a technical issue to a non-technical client?",
        "Problem Solving": "Describe a difficult bug you solved.",
        "Git": "What is git commit?",
        "GitHub": "Difference between fork and clone?",
        "OOP": "Name four pillars of OOP.",
        "DBMS": "What is normalization?"
    }

    questions = []
    for skill in skills:
        if skill in question_bank:
            questions.append((skill, question_bank[skill]))
    return questions