from resume_parser.extract_text import extract_text_from_pdf
from ml_models.predict_role import predict_role
from skill_extraction.skill_extractor import extract_skills
from ats_scoring.skill_gap_analysis import skill_gap
from ats_scoring.ats_score import calculate_score

def analyze_resume(file_path, required_skills):

    text = extract_text_from_pdf(file_path)

    role = predict_role(text)

    resume_skills = extract_skills(text)

    matched, missing = skill_gap(resume_skills, required_skills)

    score = calculate_score(matched, required_skills)

    result = {

        "predicted_role": role,
        "resume_skills": resume_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "ats_score": score

    }

    return result