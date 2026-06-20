def build_profile(profile):

    score = 0

    # Dashboard (SQLite tuple)
    if isinstance(profile, tuple):

        skills = str(profile[7]).lower()
        cgpa = float(profile[6])

    # Profile page (dictionary)
    else:

        skills = str(
            profile.get("skills", "")
        ).lower()

        cgpa = float(
            profile.get("cgpa", 0)
        )

    if "python" in skills:
        score += 20

    if "machine learning" in skills:
        score += 20

    if "deep learning" in skills:
        score += 20

    if cgpa >= 8.5:
        score += 40

    return score