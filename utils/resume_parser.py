import pdfplumber
import re

SKILLS_DB = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "SQL",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "PyTorch",
    "OpenCV",
    "Streamlit",
    "Java",
    "C",
    "Git",
    "GitHub"
]

def extract_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_skills(text):

    found_skills = []

    for skill in SKILLS_DB:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return found_skills


def extract_profile(text):

    profile = {}

    lines = text.split("\n")

    # Name (first non-empty line)
    for line in lines:

        if len(line.strip()) > 3:

            profile["name"] = line.strip()

            break

    # Degree
    degree_patterns = [
        "B.Tech",
        "Bachelor",
        "B.E",
        "M.Tech"
    ]

    profile["degree"] = ""

    for d in degree_patterns:

        if d.lower() in text.lower():

            profile["degree"] = d

            break

    # Branch
    if "Artificial Intelligence" in text:
        profile["branch"] = "AIML"

    elif "Computer Science" in text:
        profile["branch"] = "CSE"

    else:
        profile["branch"] = ""

    # CGPA
    cgpa_match = re.search(
        r'(\d\.\d{1,2})',
        text
    )

    if cgpa_match:
        profile["cgpa"] = float(
            cgpa_match.group(1)
        )

    else:
        profile["cgpa"] = 0.0

    return profile