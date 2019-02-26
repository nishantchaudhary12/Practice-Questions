#math puzzle


def add_one_in_beginning(x):
    x = 100000 + x
    return x


def add_one_in_end(y):
    y = y * 10 + 1
    return y


def compare_times_3(x,y):
    return True if y == 3 * x else False


def get_numbers():
    numbers = []
    for num in range(10000,100000):
        num_1 = add_one_in_beginning(num)
        num_2 = add_one_in_end(num)
        if compare_times_3(num_1, num_2):
            numbers.append(num)
    return numbers


print(get_numbers())




