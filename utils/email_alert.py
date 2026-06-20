import smtplib
import pandas as pd
sender_email = "sreejagurrala23@gmail.com"
sender_password = "jluyhxnxphzbqput"

receiver_email = "sreejagurrala23@gmail.com"

df = pd.read_csv("data/internships.csv")

report = ""

for _, row in df.iterrows():

    report += (
        f"{row['Lab']} - "
        f"{row['Location']} - "
        f"{row['Status']}\n"
    )

message = f"""
Subject: DRDO Internship Report

DRDO Internship Tracker Report

Open Internships:

{report}

Generated Automatically.
"""
server = smtplib.SMTP(
    "smtp.gmail.com",
    587
)

server.starttls()

server.login(
    sender_email,
    sender_password
)

server.sendmail(
    sender_email,
    receiver_email,
    message
)

server.quit()

print("Email Sent Successfully")