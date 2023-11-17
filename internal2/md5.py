import math

# Constants
T = [int(abs(math.sin(i + 1)) * 2 ** 32) & 0xFFFFFFFF for i in range(64)]
s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4

# Helper functions
def left_rotate(x, c):
    return (x << c | x >> (32 - c)) & 0xFFFFFFFF

def padding(message):
    message = bytearray(message, 'utf-8')
    ml = len(message) * 8
    message.append(0x80)
    while (len(message) * 8) % 512 != 448:
        message.append(0)
    message += ml.to_bytes(8, 'little')
    return message

# MD5 algorithm
def md5(message):
    message = padding(message)

    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]

        a, b, c, d = a0, b0, c0, d0

        for j in range(64):
            if j < 16:
                f = (b & c) | (~b & d)
                g = j
            elif j < 32:
                f = (d & b) | (~d & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * j) % 16

            d_temp = d
            d = c
            c = b
            b = b + left_rotate((a + f + T[j] + int.from_bytes(chunk[4 * g:4 * g + 4], 'little')) & 0xFFFFFFFF, s[j])
            a = d_temp

        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    return sum(x << (32 * i) for i, x in enumerate([a0, b0, c0, d0])).to_bytes(16, 'little').hex()


# Example usage
text = "Hello, this is a sample text for calculating MD5 hash!"
print("MD5 hash:", md5(text))

