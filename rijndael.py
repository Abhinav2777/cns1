from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    # Generate a random IV
    iv = get_random_bytes(AES.block_size)

    # Convert the key to bytes
    key = key.encode('utf-8')

    # Create AES object with the IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad plaintext to block size
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)

    # Encrypt padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Concatenate IV and ciphertext for later use in decryption
    encrypted_message = iv + ciphertext

    return encrypted_message

def decrypt(encrypted_message, key):
    # Extract IV from the first block
    iv = encrypted_message[:AES.block_size]

    # Convert the key to bytes
    key = key.encode('utf-8')

    # Create AES object with the IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt ciphertext (excluding the IV)
    decrypted_plaintext = cipher.decrypt(encrypted_message[AES.block_size:])

    # Unpad decrypted plaintext
    unpadded_plaintext = unpad(decrypted_plaintext, AES.block_size)
    print(type(unpadded_plaintext))
    return unpadded_plaintext.decode('utf-8')

# Example usage
plaintext = input()
key = "password1234567890abcdef"

encrypted_message = encrypt(plaintext, key)
decrypted_plaintext = decrypt(encrypted_message, key)

print("Original plaintext:", plaintext)
print("Encrypted message:", encrypted_message)
print("Decrypted plaintext:", decrypted_plaintext)
