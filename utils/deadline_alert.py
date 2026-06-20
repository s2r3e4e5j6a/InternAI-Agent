import pandas as pd

df = pd.read_csv(
    "data/internships.csv"
)

df["Deadline"] = pd.to_datetime(
    df["Deadline"],
    errors="coerce"
)

today = pd.Timestamp.today()

urgent = df[
    (df["Deadline"] - today).dt.days <= 7
]

urgent = urgent[
    (urgent["Deadline"] - today).dt.days >= 0
]

print("Urgent Opportunities:")

print(
    urgent[
        ["Lab", "Deadline", "Source"]
    ]
)