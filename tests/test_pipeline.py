from app.pipeline import run_pipeline

resume_text = "I have experience in Python, SQL, and FastAPI."
jd_text = "Looking for a Python developer with SQL and Docker knowledge."

result = run_pipeline(resume_text, jd_text)
print(result)