# Python Encryption Tool - AES, DES, RSA

This is a **Python-based encryption and decryption tool** that supports three popular encryption algorithms: **AES**, **DES**, and **RSA**. The program is **interactive and menu-driven**, allowing users to easily encrypt and decrypt messages using symmetric or asymmetric encryption.
---
## **Features**

- **AES (Advanced Encryption Standard)**
  - Symmetric encryption (same key for encryption & decryption)
  - User can provide a custom key (padded/truncated to 16 bytes)
  - Uses **EAX mode** for authentication

- **DES (Data Encryption Standard)**
  - Symmetric encryption
  - User can provide a custom key (padded/truncated to 8 bytes)
  - Uses **ECB mode** for simplicity

- **RSA (Rivest–Shamir–Adleman)**
  - Asymmetric encryption (public key encrypts, private key decrypts)
  - Automatically generates public/private key pair
  - Uses **PKCS1_OAEP padding**
  - Suitable for small messages or keys

- **Menu-driven interface**
  - Choose encryption algorithm at runtime
  - Encrypt and decrypt messages interactively

---

## **Requirements**

- Python 3.x  
- `pycryptodome` library

Install `pycryptodome` using pip:

```bash
pip install pycryptodome

How to Use
1. Run the program:

python main.py


2. You will see the menu:

=== Encryption Menu ===
1. AES
2. DES
3. RSA
4. Exit
Choose an option (1-4):

3. Follow the prompts:

AES/DES: Enter text to encrypt and provide a custom key.

RSA: Enter text to encrypt (keys are generated automatically).

The program will display:

Encrypted text

Decrypted text

Example Output
=== Encryption Menu ===
1. AES
2. DES
3. RSA
4. Exit
Choose an option (1-4): 1
Enter text to encrypt (AES): Hello World
Enter AES key (any length, will pad to 16 chars): mysecretkey
Encrypted: Rz/8R7v7o1t0kZ...
Decrypted: Hello World

Choose an option (1-4): 2
Enter text to encrypt (DES): Secret Message
Enter DES key (any length, will pad to 8 chars): key123
Encrypted: q8VJf+3YpR...
Decrypted: Secret Message

Choose an option (1-4): 3
Enter text to encrypt (RSA): Confidential
Encrypted: eKx8jU9M2Q...
Decrypted: Confidential

**Notes**

AES key must be 16 bytes (automatically padded if shorter).

DES key must be 8 bytes (automatically padded if shorter).

RSA keys are generated automatically each time the program runs.

For real-world applications, AES/EAX is secure, DES/ECB is not recommended.

**Features**

AES (Advanced Encryption Standard)

Symmetric encryption (same key for encryption & decryption)

User can provide a custom key (padded/truncated to 16 bytes)

Uses EAX mode for authentication

DES (Data Encryption Standard)

Symmetric encryption

User can provide a custom key (padded/truncated to 8 bytes)

Uses ECB mode for simplicity

RSA (Rivest–Shamir–Adleman)

Asymmetric encryption (public key encrypts, private key decrypts)

Automatically generates public/private key pair

Uses PKCS1_OAEP padding

Suitable for small messages or keys

Menu-driven interface

Choose encryption algorithm at runtime

Encrypt and decrypt messages interactively

Author

Pranav Hemant Mulik

GitHub: PranavMulik

Email: pranavmulik5@gmail.com
