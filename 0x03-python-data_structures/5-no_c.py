#!/usr/bin/python3
# removes 'C' and 'c' from string
def no_c(my_string):
    no_c_string = ""
    for x in range(len(my_string)):
        if my_string[x] != 'C' and my_string[x] != 'c':
            no_c_string += my_string[x]
    return (no_c_string)
