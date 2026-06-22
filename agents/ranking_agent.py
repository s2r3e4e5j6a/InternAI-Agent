def rank_internship(
    profile,
    internship
):

    score = 0
    reasons = []

    skills = str(
        profile["skills"]
    ).lower()

    interests = str(
        profile["interests"]
    ).lower()

    required_skills = str(
        internship["skills_required"]
    ).lower()

    source = str(
        internship["Source"]
    ).lower()

    # ===================
    # CGPA
    # ===================

    if profile["cgpa"] >= internship["cgpa_required"]:

        score += 25
        reasons.append(
            "CGPA Match"
        )

    # ===================
    # Skills
    # ===================

    matched = 0

    for skill in required_skills.split(","):

        skill = skill.strip()

        if skill and skill in skills:

            matched += 1

    score += min(
        matched * 20,
        40
    )

    if matched > 0:

        reasons.append(
            f"{matched} Skill Match"
        )

    # ===================
    # Interests
    # ===================

    if (
        "ai/ml" in interests
        and
        "machine learning"
        in required_skills
    ):

        score += 20

        reasons.append(
            "AI Interest Match"
        )

    # ===================
    # Govt Organizations
    # ===================

    if source in [
        "drdo",
        "isro",
        "barc",
        "hal",
        "bel"
    ]:

        score += 15

        reasons.append(
            "Government Opportunity"
        )

    return score, reasons