#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # using dictionary  to multiply the value of every key: value
    # pair in a dictionary
    return {key: value*2 for (key, value) in a_dictionary.items()}
