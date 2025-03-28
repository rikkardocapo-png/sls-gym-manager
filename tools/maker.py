from cryptography.fernet import Fernet
import os

# Function to generate a key (only needed once)
def generate_key():
    key = Fernet.generate_key()
    # Save the key to a file so we can use it later
    with open("ADMINAPP/utf8_encoder.key", "wb") as key_file:
        key_file.write(key)
    print(f"Encryption key generated and saved to utf8_encoder.key")

    return key

# Function to encrypt the provided credentials
def encrypt_credentials(key, host, user, password, database, port):
    cipher = Fernet(key)

    encrypted_host = cipher.encrypt(host.encode()).decode()
    encrypted_user = cipher.encrypt(user.encode()).decode()
    encrypted_password = cipher.encrypt(password.encode()).decode()
    encrypted_database = cipher.encrypt(database.encode()).decode()
    encrypted_port = cipher.encrypt(port.encode()).decode()

    # Write encrypted credentials to the .env file
    with open("CLIENTAPP/.env", "w") as env_file:
        env_file.write(f"DB_HOST={encrypted_host}\n")
        env_file.write(f"DB_USER={encrypted_user}\n")
        env_file.write(f"DB_PASSWORD={encrypted_password}\n")
        env_file.write(f"DB_DATABASE={encrypted_database}\n")
        env_file.write(f"DB_PORT={encrypted_port}\n")

    print("Credentials encrypted and stored in .env file.")

# Main program to ask for credentials, encrypt and store them
def main():
    # If you already have the key, just load it. Otherwise, generate a new one.
    if os.path.exists("ADMINAPP/utf8_encoder.key"):
        with open("ADMINAPP/utf8_encoder.key", "rb") as key_file:
            key = key_file.read()
        print("Using existing key.")
    else:
        key = generate_key()

    # Prompt the user for their credentials
    host = "sql7.freesqldatabase.com"
    user = "sql7766897"
    database = "sql7766897"
    port = "3306"
    psw = "REDACTED"


    # Encrypt and store the credentials
    encrypt_credentials(key, host, user, psw, database, port)

if __name__ == "__main__":
    main()
