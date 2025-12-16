import re

def extract_experience(text):
    """
    Extracts years of experience from resume text.
    Example matches:
    - '2 years experience'
    - '3+ years'
    - '5 yrs'
    """
    matches = re.findall(r'(\d+)\+?\s*(years|yrs)', text.lower())
    years = [int(m[0]) for m in matches]
    return max(years) if years else 0
