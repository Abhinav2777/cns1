def euclidean(x, y):
    while y:
        x, y = y, x % y

    return x

def extended_euclidean(x, y):
    if x == 0:
        return y, 0, 1

    gcd, x1, y1 = extended_euclidean(y % x, x)
    a = y1 - (y // x) * x1
    b = x1

    return gcd, a, b

a = list(map(int, input().split()))
print("Euclidean gcd", euclidean(a[0], a[1]))
gcd, x, y = extended_euclidean(a[0], a[1])
print("Extended euclidean coefficients x {} and y:{} and gcd is {}".format(x, y, gcd))
