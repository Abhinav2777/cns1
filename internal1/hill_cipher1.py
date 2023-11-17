import numpy as np
from sympy import Matrix
import math
def prepare_input(text, key_size):
    # Pad the text with extra characters if needed to make its length a multiple of key_size
    while len(text) % key_size != 0:
        text += 'X'
    return text

def generate_key_matrix(key):
    # Generate a random invertible key matrix
    # while True:
    #     key_matrix = np.random.randint(0, 26, size=(key_size, key_size))
    #     det = int(round(Matrix(key_matrix).det()))
    #     if det % 2 != 0 and det % 13 != 0:
    #         break
    # return key_matrix
    key_values = [ord(char) - ord('A') for char in key]

    # Determine the size of the square matrix
    matrix_size = math.ceil(np.sqrt(len(key_values)))

    # Pad the key if needed
    while len(key_values) < matrix_size**2:
        key_values.append(0)  # You can use any padding value, 0 is just an example

    # Reshape the list into a square matrix
    key_matrix = np.array(key_values).reshape(matrix_size, matrix_size)

    return key_matrix

def text_to_matrix(text, key_size):
    # Convert the text to a matrix of numbers based on the ASCII values
    matrix = []
    for char in text:
        matrix.append(ord(char) - ord('A'))
    return np.array(matrix).reshape(-1, key_size)

def matrix_to_text(matrix):
    # Convert the matrix of numbers back to text
    return ''.join([chr(int(num) % 26 + ord('A')) for num in matrix.flatten()])

def encrypt(plaintext, key_matrix):
    key_size = key_matrix.shape[0]
    plaintext = prepare_input(plaintext, key_size)
    plaintext_matrix = text_to_matrix(plaintext, key_size)
    ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    ciphertext = matrix_to_text(ciphertext_matrix)
    return ciphertext

def decrypt(ciphertext, key_matrix):
    key_matrix_inv = Matrix(key_matrix).inv_mod(26)
    ciphertext_matrix = text_to_matrix(ciphertext, len(key_matrix))
    plaintext_matrix = np.dot(ciphertext_matrix, key_matrix_inv) % 26
    plaintext = matrix_to_text(plaintext_matrix)
    plaintext = plaintext[:-1]
    return plaintext

# Example usage:
plaintext = "HELLO WORLD"
key_size = 5  # You can change this to any square matrix size
custom_key = "GYBNQKURP"
key_matrix = generate_key_matrix(custom_key)

# Encrypt
ciphertext = encrypt(plaintext, key_matrix)
print("Encrypted:", ciphertext)

# Decrypt
decrypted_text = decrypt(ciphertext, key_matrix)
print("Decrypted:", decrypted_text)

