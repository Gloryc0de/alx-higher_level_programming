#!/usr/bin/python3
def multiple_returns(sentence):
    # Returns a turple with the length of a string and its first chacter
    string_length = len(sentence)
    if string_length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return ((string_length, first_char))
