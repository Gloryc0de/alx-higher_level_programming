#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # prints the reverse of a given list
    if type(my_list) is list:
        y = my_list[:]
        y.reverse()
        for x in range(len(my_list)):
            print("{:d}".format(y[x]))
