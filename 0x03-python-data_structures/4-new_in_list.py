#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = len(my_list)
    if idx < 0:
        return (my_list)
    elif idx >= i:
        return (my_list)
    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
