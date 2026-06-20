import pandas as pd

def discover_opportunities():

    df = pd.read_csv(
        "data/internships.csv"
    )

    return df