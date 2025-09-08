import requests

API_KEY = "AIzaSyDUMMY-KEY-1234567890abcdef"
DB_PASSWORD = "SuperSecretPass123!"

def connect():
    print("Connecting to DB with password:", DB_PASSWORD)

def call_api():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get("https://api.example.com/data", headers=headers)
    return response.json()

if __name__ == "__main__":
    connect()
    print(call_api())
