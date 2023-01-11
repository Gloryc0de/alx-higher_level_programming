#!/usr/bin/python3
def common_elements(set_1, set_2):
    # returning a set of common elements in two sets
    return ({y for y in set_1 if y in set_2})
