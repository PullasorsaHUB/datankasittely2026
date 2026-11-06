import pandas as pd
from database.db import engine

def load_users():
    df = pd.read_sql("SELECT * FROM users", engine)
    return df

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

def analyze_users(df):
    print("Shape: ",df.shape)
    print("Head: ", df.head(2))
    print("Tail: ", df.tail(2))
    
    return df

if __name__ == "__main__":
    df = load_users()
    analyze_users(df)