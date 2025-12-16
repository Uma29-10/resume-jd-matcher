def generate_questions(resume_skills, jd_skills):
    print("DEBUG resume_skills:", resume_skills)
    print("DEBUG jd_skills:", jd_skills)

    missing = set(jd_skills) - set(resume_skills)
    matched = set(jd_skills) & set(resume_skills)

    print("DEBUG missing:", missing)
    print("DEBUG matched:", matched)

    questions = []

    for skill in missing:
        questions.append(f"Do you have experience with {skill}?")

    for skill in list(matched)[:3]:
        questions.append(f"Explain a project where you used {skill}.")

    return questions