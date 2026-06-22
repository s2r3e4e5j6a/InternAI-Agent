def internship_status(profile, internship):

    if profile["cgpa"] >= 8.0:
        return "✅ Eligible"

    elif profile["cgpa"] >= 7.0:
        return "🟡 Partial Match"

    else:
        return "❌ Not Eligible"