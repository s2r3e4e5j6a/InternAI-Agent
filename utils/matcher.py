def rank_internship(
    profile,
    internship
):

    score = 0

    skills = profile["skills"].lower()
    interests = profile["interests"].lower()

    eligibility = str(
        internship["Eligibility"]
    ).lower()

    title = str(
        internship["Lab"]
    ).lower()

    # Python
    if "python" in skills:
        score += 15

    # AI / ML
    if (
        "machine learning" in skills
        or "ai" in skills
    ):
        score += 15

    # Government interest
    if (
        "government" in interests
        and (
            "drdo" in title
            or "isro" in title
            or "barc" in title
        )
    ):
        score += 25

    # Research interest
    if (
        "research" in interests
        and (
            "research" in eligibility
            or "scientist" in eligibility
        )
    ):
        score += 20

    # CGPA
    if profile["cgpa"] >= 8.5:
        score += 25

    elif profile["cgpa"] >= 7:
        score += 15

    return min(score, 100)
# AI domain
if (
    "ai/ml" in interests
    and "artificial intelligence" in str(
        internship["Domain"]
    ).lower()
):
    score += 20

# Research domain
if (
    "research" in interests
    and "research" in str(
        internship["Domain"]
    ).lower()
):
    score += 20