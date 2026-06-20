import pandas as pd

from utils.summarizer import (
    summarize_opportunity
)

from utils.email_sender import (
    send_email
)

current_df = pd.read_csv(
    "data/internships.csv"
)

known_df = pd.read_csv(
    "data/known_opportunities.csv"
)

new_opportunities = []

for _, row in current_df.iterrows():

    if row["Lab"] not in known_df["Lab"].values:

        new_opportunities.append(
            row.to_dict()
        )

if new_opportunities:

    print(
        "NEW OPPORTUNITIES FOUND\n"
    )

    email_body = ""

    for opportunity in new_opportunities:

        summary = summarize_opportunity(
            opportunity
        )

        print(summary)

        email_body += (
            summary +
            "\n\n" +
            "=" * 50 +
            "\n\n"
        )

    print(
        "\nSending Email Alert..."
    )

    send_email(
        "New Internship Opportunity Detected",
        email_body
    )

    current_df[["Lab"]].to_csv(
        "data/known_opportunities.csv",
        index=False
    )

    print(
        "Known opportunities updated."
    )

else:

    print(
        "No New Opportunities"
    )