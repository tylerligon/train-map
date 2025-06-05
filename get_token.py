import requests
import os
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOKEN_URL = "https://testraildata.njtransit.com/api/GTFSRT/getToken"

def get_token():
    response = requests.post(
        TOKEN_URL,
        files = {
            "username": (None, USERNAME),
            "password":(None, PASSWORD),
        },
        headers = {"accept": "text/plain"}
    )

    result = response.json()
    if result.get("Authenticated") == "True":
        return result["UserToken"]
    else:
        raise Exception(f"Auth failed: {result}")
    
if __name__ == "__main__":
    token = get_token()
    with open("token.txt", "w") as f:
        f.write(token)
    print ("Token saved in token.txt")