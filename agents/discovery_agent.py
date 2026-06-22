import pandas as pd


def discover_opportunities():

    try:

        df = pd.read_csv(
            "data/internships.csv"
        )

        df.columns = (
            df.columns
            .str.strip()
        )

        return df

    except Exception as e:

        print(
            f"Error loading internships: {e}"
        )

        return pd.DataFrame()