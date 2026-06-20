def rank_internship(profile, internship):

    score = 0

    skills = profile["skills"].lower()

    eligibility = str(
        internship["Eligibility"]
    ).lower()

    interests = profile["interests"].lower()

    if "python" in skills:
        score += 20

    if "machine learning" in skills:
        score += 20

    if "deep learning" in skills:
        score += 20

    if "ai" in eligibility:
        score += 15

    if "research" in eligibility:
        score += 15

    if "government" in interests:
        score += 10

    score += profile["cgpa"] * 5

    return score