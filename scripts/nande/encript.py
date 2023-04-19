from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def get_key_from_seed(seed):
    salt_string = "sorry for what? our daddy told us not be ashamed of our rationality and intelligence, 'specially when they are a nice size and all"
    salt = salt_string.encode("utf-8")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(seed.encode()))
    return key

def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()

def decrypt(encrypted_data, seed):
    key = get_key_from_seed(seed)
    print(f"seed: {seed}")
    print(f"en_data: {encrypted_data}")
    return decrypt_data(encrypted_data, key)

def write_encoded_api_key(seed, encrypted_api_key):
    with open("deleteme_config_encoded.txt", "w") as f:
        f.write(seed + "\n")
        f.write(encrypted_api_key.decode("utf-8") + "\n")

