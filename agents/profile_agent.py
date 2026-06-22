# agents/profile_agent.py

def build_profile(profile):
    """
    Calculate a profile score based on skills and CGPA.
    Returns an integer score.
    """

    score = 0

    skills = str(
        profile.get("skills", "")
    ).lower()

    try:
        cgpa = float(
            profile.get("cgpa", 0)
        )
    except:
        cgpa = 0

    if "python" in skills:
        score += 10

    if "machine learning" in skills:
        score += 20

    if "deep learning" in skills:
        score += 20

    if cgpa >= 8.5:
        score += 15

    return score