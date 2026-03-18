from cryptography.fernet import Fernet

# Generate a key 
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load saved key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt password
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted

# Decrypt password
def decrypt_password(encrypted):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted).decode()