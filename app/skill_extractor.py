SKILLS=["python", "sql", "fastapi", "machine learning"]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]