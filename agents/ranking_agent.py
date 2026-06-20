def rank_internship(
    profile,
    internship
):

    score = 0
    reasons = []

    skills = profile["skills"].lower()

    eligibility = str(
        internship["Eligibility"]
    ).lower()

    interests = str(
        profile["interests"]
    ).lower()

    # Python Match
    if "python" in skills:
        score += 20
        reasons.append("Python Skill")

    # Machine Learning Match
    if (
        "machine learning" in skills
        or "ai" in skills
    ):
        score += 25
        reasons.append("AI/ML Skills")

    # CGPA Match
    if profile["cgpa"] >= 8.5:
        score += 20
        reasons.append("CGPA > 8.5")

    # Government Interest
    if "government" in interests:
        score += 15
        reasons.append("Government Internship Interest")

    # Research Interest
    if "research" in interests:
        score += 10
        reasons.append("Research Interest")

    # Eligibility Match
    if "python" in eligibility and "python" in skills:
        score += 10
        reasons.append("Eligibility Match")

    return score, reasons