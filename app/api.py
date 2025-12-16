from fastapi import FastAPI, UploadFile, File
import os
import shutil

from app.pipeline import run_pipeline
from app.parser import extract_text
from app.emailer import send_interview_email   # ✅ NEW IMPORT

app = FastAPI(title="Resume–JD Matcher API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/match")
async def match_resume_jd(
    resume: UploadFile = File(...),
    jd: UploadFile = File(...)
):
    # Save uploaded files
    resume_path = os.path.join(UPLOAD_DIR, resume.filename)
    jd_path = os.path.join(UPLOAD_DIR, jd.filename)

    with open(resume_path, "wb") as f:
        shutil.copyfileobj(resume.file, f)

    with open(jd_path, "wb") as f:
        shutil.copyfileobj(jd.file, f)

    # Extract text (PDF / DOCX / TXT safe)
    resume_text = extract_text(resume_path)
    jd_text = extract_text(jd_path)

    # Run pipeline
    result = run_pipeline(resume_text, jd_text)

    # 📧 AUTO EMAIL IF SHORTLISTED
    if result["status"] == "SHORTLISTED":
        send_interview_email(
            to_email="candidate@email.com",   # 🔁 replace with real email later
            questions=result["auto_questions"]
        )

    return result
