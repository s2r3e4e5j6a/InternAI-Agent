def career_advice(profile):

    interests = profile["interests"]

    if "AI/ML" in interests:
        return "Recommended: AI Research Internships"

    if "Government" in interests:
        return "Recommended: DRDO, ISRO, BARC"

    return "Explore Software Internships"   