def career_advice(profile):

    advice = []

    cgpa = profile["cgpa"]

    skills = str(
        profile["skills"]
    ).lower()

    interests = str(
        profile["interests"]
    ).lower()

    if cgpa >= 8.5:

        advice.append(
            "🎯 Strong candidate for DRDO, ISRO and BARC internships."
        )

    if "python" not in skills:

        advice.append(
            "📚 Learn Python for more internship opportunities."
        )

    if "machine learning" in skills:

        advice.append(
            "🤖 Apply for AI/ML Research Internships."
        )

    if "data science" in skills:

        advice.append(
            "📊 Apply for Data Science internships."
        )

    if "government" in interests:

        advice.append(
            "🏛 Focus on DRDO, ISRO, BARC, BEL and HAL opportunities."
        )

    if not advice:

        advice.append(
            "🚀 Continue building skills and projects."
        )

    return advice