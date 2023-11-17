import struct
def left_rotate(n, b):
    return ((n<<b) | (n >> (32 - b))) & 0xFFFFFFFF

def sha1(msg):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    ml = len(msg) * 8
    msg += b'\x80'
    while (len(msg) * 8) % 512 != 448:
        msg += b'\x00'

    msg += struct.pack('>Q', ml)
    for i in range(0, len(msg), 64):
        w = [0] * 80
        for j in range(16):
            w[j] = struct.unpack('>I', msg[i + j * 4: i + j * 4 + 4])[0]
        for j in range(16, 80):
            w[j] = left_rotate(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for j in range(80):
            if 0 <= j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + e + f + k + w[j] & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp
        
        h0 = (h0 + a) & 0xFFFFFFFF
        
        h1 = (h1 + b) & 0xFFFFFFFF

        h2 = (h2 + c) & 0xFFFFFFFF

        h3 = (h3 + d) & 0xFFFFFFFF

        h4 = (h4 + e) & 0xFFFFFFFF

    return '%08x%08x%08x%08x%08x'%(h0, h1, h2, h3, h4)


message = input("Enter message")
message = message.encode('utf-8')
print(sha1(message))



