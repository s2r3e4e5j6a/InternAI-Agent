def career_advice(profile):

    advice = []

    skills = str(
        profile["skills"]
    ).lower()

    cgpa = float(
        profile["cgpa"]
    )

    interests = str(
        profile["interests"]
    ).lower()

    if cgpa >= 8.5:

        advice.append(
            "Eligible for DRDO / ISRO Research Internships"
        )

    if "python" not in skills:

        advice.append(
            "Learn Python for Internship Opportunities"
        )

    if "machine learning" in skills:

        advice.append(
            "Apply for AI/ML Internships"
        )

    if "data science" in interests:

        advice.append(
            "Build Data Science Projects"
        )

    if "ai/ml" in interests:

        advice.append(
            "Prepare for AI Engineer Roles"
        )

    if len(advice) == 0:

        advice.append(
            "Continue Building Skills and Projects"
        )

    return advice