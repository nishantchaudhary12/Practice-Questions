#For a given string, slice it according to the Size given but make sure that it doesn't show a half word.
# For e.g. If the String is 'My name is Julie Taylor' and the size given is 15 then it should only print
# 'My name is' because there isn't enough space left to print Julie.


def slice_str(user_input, slice_len):
    init_index = 0
    new_string = ''
    for each in user_input:
        if each == ' ':
            end_index = user_input.index(each, init_index+1)
            if len(user_input[init_index:end_index]) < slice_len:
                new_string = new_string + user_input[init_index:end_index]
                slice_len = slice_len - len(user_input[init_index:end_index])
                init_index = end_index
    print(new_string)


def main():
    user_input = 'My name is Julie Taylor.'
    slice_len = 15
    slice_str(user_input, slice_len)


main()