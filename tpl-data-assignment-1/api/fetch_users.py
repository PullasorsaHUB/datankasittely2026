import requests
from config import API_URL
from database.db import SessionLocal
from database.models import User

def fetch_users():
    response = requests.get(API_URL)
    response.raise_for_status()
    users = response.json()
    return users


def save_users(users):
    session = SessionLocal()
    for user in users:
        new_user = User(
            id=user["id"],
            name=user["name"],
            username=user["username"],
            email=user["email"],
            city=user["address"]["city"],
            company_name=user["company"]["name"],
            phone=user["phone"],
            website=user["website"]
        )
        session.merge(new_user)
    session.commit()
    session.close()

if __name__ == "__main__":
    users = fetch_users()
    save_users(users)
    print(len(users))
    print(users[0])