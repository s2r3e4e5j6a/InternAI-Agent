def rank_internship(
    profile,
    internship
):

    score = 0
    reasons = []

    # ===================
    # Skills (40)
    # ===================

    user_skills = [
        s.strip().lower()
        for s in str(
            profile["skills"]
        ).split(",")
    ]

    internship_skills = [
        s.strip().lower()
        for s in str(
            internship["skills_required"]
        ).split(",")
    ]

    matched_skills = len(
        set(user_skills)
        &
        set(internship_skills)
    )

    if len(internship_skills) > 0:

        score += min(
            (
                matched_skills
                /
                len(internship_skills)
            ) * 40,
            40
        )

    if matched_skills > 0:

        reasons.append(
            f"{matched_skills} Skill Match"
        )

    # ===================
    # CGPA (25)
    # ===================

    if float(profile["cgpa"]) >= float(
        internship["cgpa_required"]
    ):

        score += 25

        reasons.append(
            "CGPA Match"
        )

    # ===================
    # Interests (20)
    # ===================

    user_interests = [
        s.strip().lower()
        for s in str(
            profile["interests"]
        ).split(",")
    ]

    internship_interests = []
    matched_interests = len(
        set(user_interests)
        &
        set(internship_interests)
    )

    if len(internship_interests) > 0:

        score += min(
            (
                matched_interests
                /
                len(internship_interests)
            ) * 20,
            20
        )

    if matched_interests > 0:

        reasons.append(
            "Interest Match"
        )

    # ===================
    # Location (15)
    # ===================

    preferred_location = str(
        internship.get(
            "Location",
            ""
        )
    ).lower()

    if preferred_location == "hyderabad":

        score += 15

        reasons.append(
            "Preferred Location"
        )

    return round(score, 2), reasons