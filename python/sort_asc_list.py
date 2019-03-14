#Write a Python program to sort a list, sorted in increasing order.


def sort_list(list_inp):
    for index_element in range(len(list_inp)-1):
        min = list_inp[index_element]
        temp = min
        for num in range(index_element+1, len(list_inp)):
            cmp = list_inp[num]
            if cmp < min:
                min = cmp
                index_min = num
        if min != temp:
            list_inp[index_element] = min
            list_inp[index_min] = temp
    return list_inp



def main():
    list_inp = [1,4,2,6,8,2,1,9,2,4]
    print(sort_list(list_inp))


main()