# scorer.py

SKILL_WEIGHTS = {
    "fastapi": 3,
    "machine learning": 3,
    "python": 2,
    "sql": 1,
    "docker": 2,
    "aws": 2
}

def skill_match_score(resume_skills, jd_skills):
    if not jd_skills:
        return 0.0

    resume_skills = [s.lower() for s in resume_skills]
    jd_skills = [s.lower() for s in jd_skills]

    score = 0
    max_score = 0

    for skill in jd_skills:
        weight = SKILL_WEIGHTS.get(skill, 1)
        max_score += weight
        if skill in resume_skills:
            score += weight

    return score / max_score if max_score else 0.0
