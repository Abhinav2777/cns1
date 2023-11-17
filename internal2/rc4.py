class RC4:
    @staticmethod
    def main():
        s = [0] * 256
        k = [0] * 256

        ptext = input("Enter the plain text: ")
        key = input("Enter the key: ")
        cipher = [0] * len(ptext)
        decipher = [0] * len(ptext)
        ki = [ord(c) for c in key]
        for i in range(255):
            s[i] = i
            k[i] = ki[i % len(key)]
        j = 0
        ptexti = [ord(c) for c in ptext]
        for i in range(255):
            j = (j + s[i] + k[i]) % 256
            s[i], s[j] = s[j], s[i]
        for l in range(len(ptext)):
            i = (l + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = s[j], s[i]
            z = s[(s[i] + s[j]) % 256]
            cipher[l] = z ^ ptexti[l]
            decipher[l] = z ^ cipher[l]
        print("Cipher text: ", end = "\n")
        RC4.display(cipher)
        print("Deciphered text: ")
        RC4.display(decipher)
    @staticmethod
    def display(msg):
        msg = [chr(i) for i in msg]
        for i in msg:
            print(i, end='')
        print("\n")
RC4.main()
