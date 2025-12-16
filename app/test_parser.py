import os
from parser import extract_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "sample_resume.txt")

print("Reading file from:", file_path)
text = extract_text(file_path)
print("OUTPUT FROM FILE:")
print(text)