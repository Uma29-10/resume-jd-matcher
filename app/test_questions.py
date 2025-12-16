from question_generator import generate_questions

resume_skills = ["python", "sql"]
jd_skills = ["python", "sql", "docker", "fastapi"]

questions = generate_questions(resume_skills, jd_skills)

print("Auto-generated Interview Questions:")
for q in questions:
    print("-", q)