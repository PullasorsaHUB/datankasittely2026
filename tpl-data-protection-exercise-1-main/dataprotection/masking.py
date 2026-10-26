import pandas as pd


def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """
    
    df = pd.DataFrame(people)
    
    parts = df["email"].str.split("@", n=1, expand=True) # Tää niiku vetää kahteenosaa s-postin @ merkin kohdasta
    df["email"] = parts[0].str.replace(".", "*", regex=True) + "@" + parts[1]
    
    df["phone"] = df["phone"].str[:-2].str.replace(".", "*", regex=True) + df["phone"].str[-2:]
    
    return df.to_dict(orient="records")