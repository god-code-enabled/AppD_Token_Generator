import json
import requests
import time
from cryptography.fernet import Fernet

def encrypt_credentials():
    with open('credentials.json', 'r') as file:
        credentials = json.load(file)

    # Check if SECRET_KEY is present and plaintext
    if credentials.get('SECRET_KEY'):
        # Generate a key and encrypt the secret key
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_secret = cipher_suite.encrypt(credentials['SECRET_KEY'].encode())

        # Update the JSON file with the encrypted secret key and encryption key
        credentials['ENCRYPTED_SECRET_KEY'] = encrypted_secret.decode()
        credentials['ENCRYPTION_KEY'] = key.decode()
        credentials.pop('SECRET_KEY', None)  # Remove the plaintext SECRET_KEY

        with open('credentials.json', 'w') as file:
            json.dump(credentials, file, indent=4)
    else:
        print("No plaintext SECRET_KEY found, or it has already been encrypted.")

def generate_token():
    with open('credentials.json', 'r') as file:
        credentials = json.load(file)

    # Decrypt the secret key if necessary
    if credentials.get('ENCRYPTED_SECRET_KEY') and credentials.get('ENCRYPTION_KEY'):
        cipher_suite = Fernet(credentials['ENCRYPTION_KEY'].encode())
        SECRET_KEY = cipher_suite.decrypt(credentials['ENCRYPTED_SECRET_KEY'].encode()).decode()
    else:
        print("No encrypted SECRET_KEY found.")
        return

    CONTROLLER_PORT = credentials.get('CONTROLLER_PORT')
    ACCOUNT_NAME = credentials.get('ACCOUNT_NAME')
    CONTROLLER_HOST = f"https://{ACCOUNT_NAME}.saas.appdynamics.com"
    CLIENT_ID = f"{credentials.get('CLIENT_NAME')}@{ACCOUNT_NAME}"

    token_endpoint = f"{CONTROLLER_HOST}:{CONTROLLER_PORT}/controller/api/oauth/access_token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": SECRET_KEY
    }

    response = requests.post(token_endpoint, data=payload)  # Use POST method here
    if response.status_code == 200:
        token_data = response.json()
        API_TOKEN = token_data.get("access_token")
        print(f'New Token: {API_TOKEN}')  # Output to console
    else:
        print(f"Failed to generate token. Status code: {response.status_code}")

# Encrypt credentials right away
encrypt_credentials()

# Generate a new token every minute
while True:
    generate_token()
    time.sleep(60)  # Wait for 1 minute
