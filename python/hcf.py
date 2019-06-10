#HCF


def hcf(num1, num2):
    flag = True
    while flag:
        rem = num2 % num1
        if rem == 0:
            flag = False
        else:
            num2 = num1
            num1 = rem
    print('HCF:', num1)


def main():
    num1 = 11
    num2 = 20
    if num1 > num2:
        hcf(num2, num1)
    elif num2 > num1:
        hcf(num1, num2)
    else:
        print('HCF:', num1)  #num1 = num2


main()

