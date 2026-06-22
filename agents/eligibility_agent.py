def check_eligibility(
    user_cgpa,
    user_skills,
    internship_cgpa,
    internship_skills

):

    # Handle empty values
    try:
        internship_cgpa = float(internship_cgpa)
    except:
        internship_cgpa = 0.0

    try:
        user_cgpa = float(user_cgpa)
    except:
        user_cgpa = 0.0

    user_skills = [
        s.strip().lower()
        for s in str(user_skills).split(",")
        if s.strip()
    ]

    internship_skills = [
        s.strip().lower()
        for s in str(internship_skills).split(",")
        if s.strip()
    ]

    matched_skills = []

    for skill in internship_skills:

        if skill in user_skills:

            matched_skills.append(skill)

    skill_match = len(matched_skills)

    total_skills = len(internship_skills)

    cgpa_ok = user_cgpa >= internship_cgpa

    # No skills specified
    if total_skills == 0:

        if cgpa_ok:
            status = "Eligible"
        else:
            status = "Not Eligible"

    # Strong match
    elif cgpa_ok and skill_match >= 1:

        status = "Eligible"

    # CGPA okay but skills weak
    elif cgpa_ok:

        status = "Partial Match"

    else:

        status = "Not Eligible"

    return {
        "status": status,
        "matched_skills": matched_skills,
        "skill_match": skill_match,
        "total_skills": total_skills
    }