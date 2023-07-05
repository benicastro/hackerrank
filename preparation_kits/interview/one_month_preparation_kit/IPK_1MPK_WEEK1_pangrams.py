# Pangrams #########################################################################################################################################################

# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case.
# Return either pangram or not pangram as appropriate.

# Function Description ###
# Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram.
# Otherwise, it should return not pangram.
# pangrams has the following parameter(s):
#   - string s: a string to test
# Returns
#   - string: either pangram or not pangram

# Input Format ###

# A single line with string s.

# CODE #############################################################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    # Write your code here
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    for letter in alphabet:
        if letter not in s.lower():
            return "not pangram"
    return "pangram"

    # if len({i.lower() for i in s if i.isalpha()}) == 26:
    #     return "pangram"
    # else:
    #     return "not pangram"


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = pangrams(s)

    print(result + "\n")

    # fptr.write(result + "\n")

    # fptr.close()


# def birthday(s, d, m):
#     # Write your code here
#     seg = [sum(s[i : i + m]) == d for i in range(0, len(s)) if i + m < len(s) + 1]

#     return seg.count(True)


# def strings_xor(s, t):
#     res = ""
#     for i in range(len(s)):
#         if s[i] == t[i]:
#             res += "0"
#         else:
#             res += "1"

#     return res


# s = input()
# t = input()
# print(strings_xor(s, t))
