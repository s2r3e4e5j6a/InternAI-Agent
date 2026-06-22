def build_profile(profile):

    if not profile:
        return 0

    score = 0

    # Profile from SQLite (tuple)
    if isinstance(profile, tuple):

        skills = str(profile[7] or "").lower()
        cgpa = float(profile[6] or 0)

    # Profile from Profile Page (dictionary)
    elif isinstance(profile, dict):

        skills = str(
            profile.get("skills", "")
        ).lower()

        cgpa = float(
            profile.get("cgpa", 0)
        )

    else:
        return 0

    if "python" in skills:
        score += 20

    if "machine learning" in skills:
        score += 20

    if "deep learning" in skills:
        score += 20

    if cgpa >= 8.5:
        score += 40

    return min(score, 100)