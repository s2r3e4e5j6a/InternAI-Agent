def check_eligibility(
    profile,
    internship
):

    cgpa = profile["cgpa"]

    if cgpa >= 7.0:
        return True

    return False