Project Overview

This project automates resume screening by parsing candidate resumes and job descriptions, extracting skills and experience, computing a match score, auto-generating interview questions, and emailing shortlisted candidates.
The system helps recruiters reduce manual screening time, improve consistency, and speed up the hiring process.

Features

Resume & Job Description parsing (PDF / DOCX / TXT)
Skill extraction using rule-based matching
Skill match scoring with configurable threshold logic
Automatic shortlisting of candidates
Auto-generation of interview screening questions
Email automation for shortlisted candidates
REST API built using FastAPI
Unit tests for core logic using pytest

Tech Stack & Libraries

Python
FastAPI
PyPDF2
python-docx
smtplib (Email automation)
pytest (Unit testing)

One-Page Design Document
Motivation / Problem Context
Recruiters spend significant time manually screening resumes against job descriptions, leading to inefficiency and inconsistency.
The goal of this project is to automate resume screening and shortlisting using rule-based intelligence.

System Architecture

Resume Parser: Extracts text from PDF/DOCX resumes
Skill & Experience Extractor: Identifies relevant skills and experience keywords
Scoring Engine: Computes match score between resume and JD
Threshold Logic: Shortlists candidates based on configurable score
Question Generator: Creates interview questions dynamically
Email Service: Sends interview questions automatically
REST API: Exposes functionality using FastAPI


Data Flow
Resume → Parsing → Skill Extraction → Scoring → Threshold Check   → Question Generation → Email Trigger


Key Logic

Weighted scoring is applied based on skill overlap and experience relevance.
Candidates meeting the defined threshold are automatically shortlisted and contacted via email.


Outcome

The system reduces manual effort, improves consistency, and speeds up resume screening and candidate shortlisting.

Environment Setup & Steps to Run
Prerequisites
Python 3.8 or above
pip package manager


Steps to Run the Project

1. Clone the repository

git clone https://github.com/Uma29-10/resume-jd-matcher.git
cd resume-jd-matcher

2. pip install -r requirements.txt
pip install -r requirements.txt

3. Run the FastAPI application
uvicorn app.api:app --reload

4. Open the API in browser
http://127.0.0.1:8000/docs

5. Upload resume and job description files
Use the /match endpoint
The API returns:
Extracted skills
Match score
Shortlisting decision
Auto-generated interview questions


Testing
Unit tests are implemented using pytest to validate:
Resume parsing
Skill extraction
Scoring logic
Pipeline execution

GitHub Repository
https://github.com/Uma29-10/resume-jd-matcher