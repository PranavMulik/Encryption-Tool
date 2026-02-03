# main.py
from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

# ---------------- AES ----------------
def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def aes_decrypt(cipher_text, key):
    raw = base64.b64decode(cipher_text)
    nonce = raw[:16]
    ciphertext = raw[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode('utf-8')

# ---------------- DES ----------------
def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    while len(plain_text) % 8 != 0:
        plain_text += ' '
    ciphertext = cipher.encrypt(plain_text.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

def des_decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decoded = base64.b64decode(cipher_text)
    plain_text = cipher.decrypt(decoded).decode('utf-8')
    return plain_text.rstrip()

# ---------------- RSA ----------------
def rsa_generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(plain_text, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plain_text.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

def rsa_decrypt(cipher_text, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decoded = base64.b64decode(cipher_text)
    return cipher.decrypt(decoded).decode('utf-8')

# ---------------- Menu ----------------
def menu():
    print("\n=== Encryption Menu ===")
    print("1. AES")
    print("2. DES")
    print("3. RSA")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    return choice

def main():
    while True:
        choice = menu()
        
        if choice == '1':
            text = input("Enter text to encrypt (AES): ")
            key = get_random_bytes(16)  # AES-128 key
            encrypted = aes_encrypt(text, key)
            decrypted = aes_decrypt(encrypted, key)
            print("Encrypted:", encrypted)
            print("Decrypted:", decrypted)
        
        elif choice == '2':
            text = input("Enter text to encrypt (DES): ")
            key = b'8bytekey'  # DES key must be 8 bytes
            encrypted = des_encrypt(text, key)
            decrypted = des_decrypt(encrypted, key)
            print("Encrypted:", encrypted)
            print("Decrypted:", decrypted)
        
        elif choice == '3':
            text = input("Enter text to encrypt (RSA): ")
            private_key, public_key = rsa_generate_keys()
            encrypted = rsa_encrypt(text, public_key)
            decrypted = rsa_decrypt(encrypted, private_key)
            print("Encrypted:", encrypted)
            print("Decrypted:", decrypted)
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please select 1-4.")

if __name__ == "__main__":
    main()
