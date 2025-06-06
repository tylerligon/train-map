import requests
import pwinput
TOKEN_URL = "https://testraildata.njtransit.com/api/GTFSRT/getToken"

def get_token(username, password):
    response = requests.post(
        TOKEN_URL,
        files = {
            "username": (None, username),
            "password":(None, password),
        },
        headers = {"accept": "text/plain"}
    )

    result = response.json()
    if result.get("Authenticated") == "True":
        return result["UserToken"]
    else:
        raise Exception(f"Auth failed: {result}")
    
if __name__ == "__main__":
    username = input("Enter username: ")
    password = pwinput.pwinput(prompt = "Enter password: ", mask = "*")
    token = get_token(username, password)
    with open("token.txt", "w") as f:
        f.write(token)
    print ("Token saved in token.txt")