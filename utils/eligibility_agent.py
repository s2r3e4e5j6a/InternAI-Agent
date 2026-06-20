def calculate_match(profile, internship):

    score = 0

    skills = profile["skills"].lower()
    interests = profile["interests"].lower()

    title = internship["Title"].lower()

    if "python" in skills:
        score += 20

    if "machine learning" in skills:
        score += 20

    if "ai" in interests and (
        "ai" in title
        or "machine learning" in title
    ):
        score += 25

    if profile["cgpa"] >= 8.5:
        score += 20

    return min(score, 100)