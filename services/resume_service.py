from utils.pdf_parser import extract_text
from services.skill_service import analyze_skills


def analyze_resume(filepath, role):

    text = extract_text(filepath)

    matched, missing, score = analyze_skills(text, role)

    recommendation = "Good profile ✅" if score >= 70 else "Improve missing skills ⚠️"

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "score": score,
        "recommendation": recommendation
    }