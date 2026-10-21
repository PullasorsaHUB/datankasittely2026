from datetime import datetime
import pandas as pd

def anonymize(people):
    """
    TODO: Anonymize data:
    - remove name
    - keep only birth year
    - keep only first letter of city
    - return same datastructure with anonymized data
    """

    df = pd.DataFrame(people)
    df = df.drop(columns=["name"])
    df["birth_year"] = pd.to_datetime(df["birthdate"]).dt.year
    df["city_initial"] = df["city"].str[0]
    return df[["birth_year", "city_initial"]].to_dict(orient="records")