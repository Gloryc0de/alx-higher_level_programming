#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # finds all multiples of 2 in a list and returns
    # true or false if it is a multiple of 2 in the list
    list_length = len(my_list)
    if list_length == 0:
        return (None)
    result_list = []
    for x in range(list_length):
        if my_list[x] % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return (result_list)
