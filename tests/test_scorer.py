from scorer import skill_match_score

resume_skills = ["python", "sql", "fastapi"]
jd_skills = ["python", "fastapi", "docker"]

score = skill_match_score(resume_skills, jd_skills)
print("Skill Match Score:",score)