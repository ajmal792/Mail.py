import requests

def get_domain():
    response = requests.get("https://api.mail.tm/domains")
    data = response.json()
    return data['hydra:member'][0]['domain']

def create_account(email, password):
    url = "https://api.mail.tm/accounts"
    payload = {"address": email, "password": password}
    response = requests.post(url, json=payload)
    return response.json()

def get_token(email, password):
    url = "https://api.mail.tm/token"
    payload = {"address": email, "password": password}
    response = requests.post(url, json=payload)
    return response.json()

def get_messages(token):
    url = "https://api.mail.tm/messages"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    domain = get_domain()
    username = "randomuser"
    password = "StrongPassword123"
    email = f"{username}@{domain}"

    print(f"Creating account: {email}")
    account = create_account(email, password)
    print("Account created:", account)

    print("Getting token...")
    token_response = get_token(email, password)
    token = token_response.get("token")
    if token:
        print("Token received!")
        print("Getting messages for your temp mailbox...")
        messages = get_messages(token)
        print(messages)
    else:
        print("Failed to get token. Error:", token_response)