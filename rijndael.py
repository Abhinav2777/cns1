from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad

# Encryption
def encrypt(plain_text, password):
    salt = get_random_bytes(AES.block_size)
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return salt + cipher.iv + cipher_text

# Decryption
def decrypt(enc_text, password):
    salt = enc_text[:AES.block_size]
    iv = enc_text[AES.block_size:AES.block_size*2]
    cipher_text = enc_text[AES.block_size*2:]
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return plain_text.decode('utf-8')

# Example usage:
password = "mysecretkey"
message = "Hello, AES!"

encrypted = encrypt(message, password)
print(f"Encrypted: {encrypted}")

decrypted = decrypt(encrypted, password)
print(f"Decrypted: {decrypted}")

