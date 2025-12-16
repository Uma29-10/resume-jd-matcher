🔍 Project Overview

This project automates resume screening by parsing candidate resumes and job descriptions, extracting skills, computing a match score, auto-generating interview questions, and emailing shortlisted candidates.

The system helps recruiters reduce manual screening time and improve consistency.


---

⚙ Features

Resume & JD parsing (TXT / PDF ready)

Skill extraction

Skill match scoring with threshold logic

Auto-generated interview questions

Email automation for shortlisted candidates

REST API using FastAPI



---

🛠 Tech Stack & Libraries

Python

FastAPI

PyPDF2, python-docx

smtplib (email automation)

pytest (unit testing)

---

## Resume–JD Matcher: One-Page Design Document

### Motivation / Problem Context
Recruiters spend significant time manually screening resumes against job descriptions, leading to inefficiency and inconsistency. The goal of this project is to automate resume screening and shortlisting using rule-based intelligence.

### System Architecture
- Resume Parser: Extracts text from PDF/DOCX resumes
- Skill & Experience Extractor: Identifies relevant skills and experience keywords
- Scoring Engine: Computes match score between resume and JD
- Threshold Logic: Shortlists candidates based on configurable score
- Question Generator: Creates interview questions dynamically
- Email Service: Sends interview questions automatically

### Data Flow
Resume → Parsing → Skill Extraction → Scoring → Threshold Check → Question Generation → Email Trigger

### Key Logic
Weighted scoring is applied based on skill overlap and experience relevance. Candidates meeting the threshold are automatically shortlisted and contacted.

### Outcome
The system reduces manual effort, improves consistency, and speeds up resume screening.