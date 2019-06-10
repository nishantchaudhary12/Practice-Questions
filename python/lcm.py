#LCM


def lcm(num1, num2):
    numbers = [(num1, num2)]
    factors = list()
    for num in range(2, num2+1):
        while numbers[0][0] % num == 0 and numbers[0][1] % num == 0:
            num1 = numbers[0][0] // num
            num2 = numbers[0][1] // num
            numbers = [(num1, num2)]
            factors.append(num)
        while numbers[0][1] % num == 0:
            num2 = numbers[0][1] // num
            num1 = numbers[0][0]
            numbers = [(num1, num2)]
            factors.append(num)
        while numbers[0][0] % num == 0:
            num1 = numbers[0][0] // num
            num2 = numbers[0][1]
            numbers = [(num1, num2)]
            factors.append(num)

        if num1 == 1 and num2 == 1:
            # flag = False
            break

    product = 1
    for each in factors:
        product *= each

    print('LCM:', product)


def main():
    num1 = 11
    num2 = 20
    if num1 >= num2:
        lcm(num2, num1)
    elif num2 > num1:
        lcm(num1, num2)


main()


'''Another method
if x >= y:
    greater = x
else:
    greater = y
while True:
    if (greater % x == 0) and (greater % y == 0):
        hcf = greater
        break
    greater += 1
'''