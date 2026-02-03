Python Encryption Tool - AES, DES, RSA
This is a Python-based encryption and decryption tool that supports three popular encryption algorithms: AES, DES, and RSA. The program is interactive and menu-driven, allowing users to easily encrypt and decrypt messages using symmetric or asymmetric encryption.

![Alternative Text](URL_OF_IMAGE)

Features
AES (Advanced Encryption Standard)
Symmetric encryption: Uses the same key for encryption and decryption.

Custom Keys: Users can provide a custom key (automatically padded or truncated to 16 bytes).

Secure Mode: Uses EAX mode for authenticated encryption.

DES (Data Encryption Standard)
Symmetric encryption: Traditional symmetric algorithm.

Custom Keys: Users can provide a custom key (padded or truncated to 8 bytes).

Mode: Uses ECB mode for simplicity.

RSA (Rivest–Shamir–Adleman)
Asymmetric encryption: Uses a public key to encrypt and a private key to decrypt.

Automatic Key Gen: Automatically generates a public/private key pair.

Padding: Uses PKCS1_OAEP padding for enhanced security.

Usage: Best suited for small messages or encrypting other keys.

General Features
Menu-driven interface: Choose your algorithm at runtime.

Interactive: Encrypt and decrypt messages step-by-step.

Requirements
Python 3.x

pycryptodome library

Install pycryptodome using pip:

Bash
pip install pycryptodome
How to Use
Run the program by typing:

Bash
python main.py
Navigate the menu:

=== Encryption Menu ===

AES

DES

RSA

Exit

Follow the prompts:

For AES/DES: Enter the text you want to encrypt and provide your chosen key.

For RSA: Simply enter the text; the program handles the key generation for you.

View Results: The program will display the Encrypted text and then immediately verify it by showing the Decrypted text.

Example Output
AES Selection:

Choose an option (1-4): 1

Enter text to encrypt (AES): Hello World

Enter AES key: mysecretkey

Encrypted: Rz/8R7v7o1t0kZ...

Decrypted: Hello World

RSA Selection:

Choose an option (1-4): 3

Enter text to encrypt (RSA): Confidential

Encrypted: eKx8jU9M2Q...

Decrypted: Confidential

Important Notes
Padding: AES keys are automatically padded to 16 bytes, and DES keys to 8 bytes.

RSA Keys: New keys are generated every time the program runs; they are not saved to disk in this version.

Security Warning: While this tool is great for learning, DES/ECB is considered insecure for modern sensitive data. AES/EAX is the recommended choice for security.

Author
Pranav Hemant Mulik

GitHub: PranavMulik

Email: pranavmulik5@gmail.com
