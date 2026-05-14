from flask import Flask, render_template, request, jsonify
import os
from utils.pdf_parser import extract_text
from services.skill_service import analyze_skills

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Job roles with REQUIRED SKILLS
JOB_ROLES = {
    "SDE": [
        "python", "java", "c++", "data structures",
        "algorithms", "oops", "sql", "git"
    ],
    "Data Scientist": [
        "python", "statistics", "machine learning",
        "pandas", "numpy", "data analysis"
    ],
    "ML Engineer": [
        "python", "machine learning",
        "deep learning", "tensorflow", "pytorch"
    ],
    "Web Developer": [
        "html", "css", "javascript",
        "react", "flask", "django"
    ]
}


@app.route("/", methods=["GET", "POST"])
def index():
    extracted_skills = []
    matched_skills = []
    missing_skills = []
    suitability = 0
    selected_role = None

    if request.method == "POST":
        selected_role = request.form.get("role")
        file = request.files.get("resume")

        if file and selected_role:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            # Extract resume text
            resume_text = extract_text(filepath).lower()

            # Extracted skills (normalized)
            extracted_skills = matched_skills  # For now, set to matched

            required_skills = JOB_ROLES[selected_role]

            # ✔ CORRECT matching logic
            for skill in required_skills:
                if skill.lower() in resume_text:
                    matched_skills.append(skill)

            missing_skills = [skill for skill in required_skills if skill not in matched_skills]

            suitability = int((len(matched_skills) / len(required_skills)) * 100)

    return render_template(
        "index.html",
        roles=JOB_ROLES.keys(),
        extracted_skills=extracted_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        suitability=suitability,
        selected_role=selected_role
    )


@app.route("/api/upload", methods=["POST"])
def api_upload():
    selected_role = request.form.get("role")
    file = request.files.get("resume")

    if not file or not selected_role:
        return jsonify({"error": "Missing file or role"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    resume_text = extract_text(filepath).lower()

    required_skills = JOB_ROLES.get(selected_role, [])

    matched_skills = []
    for skill in required_skills:
        if skill.lower() in resume_text:
            matched_skills.append(skill)

    missing_skills = [skill for skill in required_skills if skill not in matched_skills]

    suitability = int((len(matched_skills) / len(required_skills)) * 100) if required_skills else 0

    recommendation = "Good profile ✅" if suitability >= 70 else "Improve missing skills ⚠️"

    return jsonify({
        "score": suitability,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendation": recommendation
    })


if __name__ == "__main__":
    app.run(debug=True)
