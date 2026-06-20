def build_profile(profile):

    score = 0

    skills = profile["skills"].lower()

    if "python" in skills:
        score += 10

    if "machine learning" in skills:
        score += 20

    if "deep learning" in skills:
        score += 20

    if profile["cgpa"] >= 8.5:
        score += 15

    return {
        "profile_score": score,
        "interests": profile["interests"]
    }