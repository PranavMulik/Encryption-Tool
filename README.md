# Python Encryption Tool - AES, DES, RSA

This is a **Python-based encryption and decryption tool** that supports three popular encryption algorithms: **AES**, **DES**, and **RSA**. The program is **interactive and menu-driven**, allowing users to easily encrypt and decrypt messages using symmetric or asymmetric encryption.

![Uploading Project.jpg…]()



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

pip install pycryptodome

---

## **How to Use**

1. Run the program

2. Open your terminal or command prompt and run:

python main.py

3. Menu Selection

4. You will see the following menu:

=== Encryption Menu ===
1. AES
2. DES
3. RSA
4. Exit
Choose an option (1-4):


Enter the number corresponding to the encryption algorithm you want to use.

## **Follow the Prompts**

AES / DES: Enter the text you want to encrypt and provide a custom key. The program will automatically pad or truncate the key to the required length.

RSA: Enter the text you want to encrypt. The program generates a public/private key pair automatically.

## **View Results**
The program will display:

Encrypted text

Decrypted text

Example Output

AES:

Enter text to encrypt (AES): Hello World
Enter AES key (any length, will pad to 16 chars): mysecretkey
Encrypted: Rz/8R7v7o1t0kZ...
Decrypted: Hello World


DES:

Enter text to encrypt (DES): Secret Message
Enter DES key (any length, will pad to 8 chars): key123
Encrypted: q8VJf+3YpR...
Decrypted: Secret Message


RSA:

Enter text to encrypt (RSA): Confidential
Encrypted: eKx8jU9M2Q...
Decrypted: Confidential


## **Notes**

AES key must be 16 bytes (automatically padded if shorter).

DES key must be 8 bytes (automatically padded if shorter).

RSA keys are generated automatically each time the program runs.

For real-world applications, AES with EAX mode is secure; DES with ECB mode is not recommended.

## **Features**

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

---

**Author**

Pranav Hemant Mulik

GitHub: PranavMulik

Email: pranavmulik5@gmail.com






