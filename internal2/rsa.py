import math
def gcd(a, b):
    while (b != 0):
        a, b = b, a % b
    return a

def rsa(let):
    p, q = 3, 7
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while (e < phi):
        if (gcd(e, phi) == 1):
            break
        else:
            e += 1
    print(e)
    k = 2
    d = (1 + (k * phi))/e
    cipher = pow(let, e)
    print(cipher)
    cipher = math.fmod(cipher, n)
    print("Cipher text is : ", cipher)
    pt = pow(cipher, d)
    pt = math.fmod(pt, n)

    print("Original message is: ", pt)

rsa(12.0)
