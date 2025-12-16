# emailer.py
import smtplib
import os
from email.message import EmailMessage

def send_interview_email(to_email, questions):
    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("EMAIL_APP_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = "Interview Screening Questions"
    msg["From"] = sender_email
    msg["To"] = to_email

    body = "Please answer the following interview questions:\n\n"
    for q in questions:
        body += f"- {q}\n"

    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
