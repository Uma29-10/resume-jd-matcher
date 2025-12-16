from app.skill_extractor import extract_skills
from app.scorer import skill_match_score
from app.question_generator import generate_questions
from app.experience_extractor import extract_experience

THRESHOLD = 70

def run_pipeline(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    skill_score = skill_match_score(resume_skills, jd_skills) * 100

    resume_exp = extract_experience(resume_text)
    jd_exp = extract_experience(jd_text)

    exp_score = 100 if resume_exp >= jd_exp else (resume_exp / max(jd_exp, 1)) * 100

    final_score = 0.7 * skill_score + 0.3 * exp_score

    status = "SHORTLISTED" if final_score >= THRESHOLD else "REJECTED"

    questions = generate_questions(resume_skills, jd_skills)

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "skill_score": round(skill_score, 2),
        "experience_score": round(exp_score, 2),
        "match_score": round(final_score, 2),
        "status": status,
        "auto_questions": questions
    }
