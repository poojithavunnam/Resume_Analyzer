ROLE_SKILLS = {
    "sde": [
        "python", "sql", "flask", "git",
        "data structures", "algorithms",
        "mysql", "html", "css"
    ],

    "data_analyst": [
        "python", "sql", "excel",
        "statistics", "pandas",
        "data visualization"
    ],

    "ml_engineer": [
        "python", "machine learning",
        "tensorflow", "deep learning",
        "numpy", "pandas"
    ]
}


def analyze_skills(text, role):

    text = text.lower()

    required_skills = ROLE_SKILLS.get(role, [])

    matched = []
    missing = []

    for skill in required_skills:
        if skill in text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(required_skills)) * 100) if required_skills else 0

    return matched, missing, score