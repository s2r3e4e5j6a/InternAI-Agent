from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import pandas as pd


def generate_pdf():

    df = pd.read_csv(
        "data/internships.csv"
    )

    pdf = SimpleDocTemplate(
        "Internship_Report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "DRDO Internship Tracker Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 12)
    )

    for _, row in df.iterrows():

        text = (
            f"{row['Lab']} | "
            f"{row['Location']} | "
            f"{row['Status']}"
        )

        content.append(
            Paragraph(
                text,
                styles["BodyText"]
            )
        )

    pdf.build(content)

    return "Internship_Report.pdf"