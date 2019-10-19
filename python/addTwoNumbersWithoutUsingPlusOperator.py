def add(x, y):
    if x != y:
        return (x * x - y * y) // (x - y)
    else:
        return 2 * x


a = 10
b = 22
print('Sum:', add(a, b))