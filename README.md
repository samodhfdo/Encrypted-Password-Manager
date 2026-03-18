# Encrypted Password Manager

A secure and easy-to-use **Python password manager** that allows you to safely store and retrieve your passwords. All passwords are encrypted using **cryptography** and stored securely in a JSON file.

---

## Features

- Add new account passwords securely
- Retrieve saved passwords
- Passwords are encrypted using **Fernet symmetric encryption**
- Stores all data in a JSON file
- Modular and clean Python code structure

---

## Technologies Used

- **Python 3.13**  
- **cryptography** library (`Fernet`) for password encryption and decryption  
- **JSON** for lightweight data storage  
- Modular code with `utils` folder for encryption and storage  
- File handling and exception handling

---

## How It Works

1. **Encryption:** Passwords entered by the user are encrypted using a secret key (`Fernet`) before storage.  
2. **Storage:** Encrypted passwords are stored in `passwords.json` as key-value pairs.  
3. **Decryption:** When retrieving passwords, the program decrypts them using the same secret key.  

---

## Usage

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/Encrypted-Password-Manager.git
