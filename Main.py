from utils.encryption import generate_key, encrypt_password, decrypt_password
from utils.storage import save_password, get_password

generate_key()
while True:
    print("\n Password Manager ")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        account = input("Enter account name: ")
        password = input("Enter password: ")
        encrypted = encrypt_password(password)
        save_password(account, encrypted.decode())
        print(f"Password for '{account}' saved securely!")

    elif choice == "2":
        account = input("Enter account name: ")
        encrypted = get_password(account)
        if encrypted:
            print(f"Password for '{account}': {decrypt_password(encrypted.encode())}")
        else:
            print("Account not found!")

    elif choice == "3":
        print("Exiting Password Manager...")
        break

    else:
        print("Invalid choice!")