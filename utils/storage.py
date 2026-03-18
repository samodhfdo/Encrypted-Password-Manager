import json

FILE_NAME = "passwords.json"

# Save a new password
def save_password(account, password):
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[account] = password
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Retrieve password
def get_password(account):
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
        return data.get(account, None)
    except FileNotFoundError:
        return None