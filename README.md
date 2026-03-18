# Encrypted Password Manager 🔒

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python) ![GitHub](https://img.shields.io/badge/GitHub-Repo-black?logo=github)

A **secure and modular Python password manager** that encrypts your passwords using **Fernet encryption** and stores them safely in a JSON file. Ideal for learning encryption, file handling, and modular coding.

---

## 🚀 Features

- Add new account passwords securely  
- Retrieve saved passwords  
- All passwords are encrypted using **Fernet symmetric encryption**  
- Stored in **JSON** for lightweight, portable storage  
- Clean, modular Python code (`utils/encryption.py` & `utils/storage.py`)  
- Error handling and secure file management  

---

## 🛠️ Technologies Used

- **Python 3.13**  
- **cryptography** library (`Fernet`)  
- **JSON** file storage  
- Modular code structure  
- File handling and exception handling  

---

## 🖥️ Demo (Optional)

Add a screenshot or GIF of your program running here:

![Demo](screenshot.png)  
> Example: main menu and adding/retrieving passwords  

---

## ⚡ How It Works

1. **Encryption:** User passwords are encrypted using a **secret key (`Fernet`)**.  
2. **Storage:** Encrypted passwords are saved in `passwords.json`.  
3. **Decryption:** Passwords are decrypted when retrieved using the same secret key.  

---

## 📂 Folder Structure

```text
Encrypted Password Manager/
│── main.py
│── passwords.json (auto-created)
│── secret.key (auto-created)
│── utils/
    │── encryption.py
    │── storage.py
