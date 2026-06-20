import pandas as pd

from sources.hal import get_hal_data
from sources.bel import get_bel_data
from sources.drdo import get_drdo_data
from sources.isro import get_isro_data
from sources.barc import get_barc_data
from extractors.start_parser import get_start_data


def process_data(data):

    today = pd.Timestamp.today()

    for internship in data:

        deadline_value = str(
            internship.get(
                "Deadline",
                "Unknown"
            )
        ).strip()

        if (
            deadline_value == ""
            or deadline_value.lower() == "unknown"
            or deadline_value.lower() == "deadline"
        ):

            internship["Days Left"] = -1
            internship["Status"] = "Open"

            continue

        deadline = pd.to_datetime(
            deadline_value,
            errors="coerce"
        )

        if pd.isna(deadline):

            internship["Days Left"] = -1
            internship["Status"] = "Open"

            continue

        days_left = (
            deadline - today
        ).days

        internship["Days Left"] = days_left

        if days_left < 0:

            internship["Status"] = "Expired"

        elif days_left <= 15:

            internship["Status"] = "Closing Soon"

        else:

            internship["Status"] = "Open"

    return data


data = []

data.extend(get_hal_data())
data.extend(get_bel_data())
data.extend(get_drdo_data())
data.extend(get_isro_data())
data.extend(get_barc_data())
data.extend(get_start_data())

print(
    "Opportunities Found:",
    len(data)
)

data = process_data(data)

df = pd.DataFrame(data)

df.to_csv(
    "data/internships.csv",
    index=False
)

print(
    "CSV Updated Successfully"
)