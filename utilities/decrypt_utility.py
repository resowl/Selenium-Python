from cryptography.fernet import Fernet
from configuration import config
import os.path

def decrypt_text (text) :
    if os.path.exists(config.TestData.PROJECT_ENCRYPT_KEY_PATH):
        print("Key Found")
        with open(config.TestData.PROJECT_ENCRYPT_KEY_PATH, "rb") as keyFile:
            key = keyFile.read()

        fernet_obj = Fernet(key)
        decrypted_message = fernet_obj.decrypt(text.encode()).decode()
        return decrypted_message
    else:
        # Write fail-safe/retry mechanism here when key is not available
        print("KEY NOT FOUND")
        return text

