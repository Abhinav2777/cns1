# Python3 implementation of 
# Columnar Transposition
import math

# Columnar.py
class Columnar:
    @staticmethod
    def encrypt(msg, key):
        cipher = ""

        # track key indices
        k_indx = 0

        msg_len = float(len(msg))
        msg_lst = list(msg)
        key_lst = sorted(list(key))

        # calculate column of the matrix
        col = len(key)

        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))

        # add the padding character '_' in empty
        # the empty cell of the matix 
        fill_null = int((row * col) - msg_len)
        msg_lst.extend('_' * fill_null)

        # create Matrix and insert message and 
        # padding characters row-wise 
        matrix = [msg_lst[i: i + col] 
                for i in range(0, len(msg_lst), col)]

        # read matrix column-wise using key
        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
            cipher += ''.join([row[curr_idx] 
                            for row in matrix])
            k_indx += 1

        return cipher

    @staticmethod
    def decrypt(cipher, key):
        msg = ""

        # track key indices
        k_indx = 0

        # track msg indices
        msg_indx = 0
        msg_len = float(len(cipher))
        msg_lst = list(cipher)

        # calculate column of the matrix
        col = len(key)

        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))

        # convert key into list and sort 
        # alphabetically so we can access 
        # each character by its alphabetical position.
        key_lst = sorted(list(key))

        # create an empty matrix to 
        # store deciphered message
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]

        # Arrange the matrix column wise according 
        # to permutation order by adding into new matrix
        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])

            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
            k_indx += 1

        # convert decrypted msg matrix into a string
        try:
            msg = ''.join(sum(dec_cipher, []))
        except TypeError:
            raise TypeError("This program cannot",
                            "handle repeating words.")

        null_count = msg.count('_')

        if null_count > 0:
            return msg[: -null_count]

        return msg


# Advanced Columnar Cipher
class Adv_Columnar:
    def main(self):
        message = "Hello CSE5"
        key = "megabuck"
        iterations = 9

        adv_c = Adv_Columnar()

        cipher = adv_c.encrypt(message, key, iterations)
        decrypted = adv_c.decrypt(cipher, key, iterations)

        print("Message:", message)
        print("Key:", key)
        print("Iterations:", iterations)
        print("CipherText:", cipher)
        print("Decrypted:", decrypted)

    def encrypt(self, message, key, iterations):
        cipher = message

        # Note Columnar.py is required for this
        for _ in range(iterations):
            cipher = Columnar.encrypt(cipher, key)

        return cipher

    def decrypt(self, cipher, key, iterations):
        message = cipher

        for _ in range(iterations):
            message = Columnar.decrypt(message, key)

        message = message.replace('-', ' ')

        return message


# Example of how to use the Adv_Columnar class:
adv_c_instance = Adv_Columnar()
adv_c_instance.main()

