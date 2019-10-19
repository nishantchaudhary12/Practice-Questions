def add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1

    return x


a = 10
b = 22
print('Sum:', add(a, b))