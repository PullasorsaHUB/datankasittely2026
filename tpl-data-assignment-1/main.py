from api.fetch_users import fetch_users, save_users
from data_protection.masking import mask_phone, mask_name
from data_analysis.analysis import load_users, analyze_users

def main():
    data = fetch_users()
    save_users(data)
    df = load_users()
    df["phone"] = df["phone"].apply(mask_phone)
    df["name"] = df["name"].apply(mask_name)
    analyze_users(df)
    
    
if __name__ == "__main__":
    main()