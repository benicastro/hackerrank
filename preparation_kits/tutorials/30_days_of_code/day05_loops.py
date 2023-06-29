# Day 5: Loops #####################################################################################################################

# Objective ###
# In this challenge, we will use loops to do some math.

# Task ###
# Given an integer, n, print its first  multiples. Each multiple n x i (where 1 <= i <= 10) should be printed on a
# new line in the form: n x i = result.

# Input Format ###
# A single integer, n.

# Output Format ###

# Print 10 lines of output; each line i (where 1 <= i <= 10) contains the result of n x i  in the form:
# n x i = result.

# CODE #############################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys


def print_multiples(n):
    ### This function prints the multiples of the input n
    # for i in range(1, 11):
    #     print(f"{n} x {i} = {n*i}")
    print(*map(lambda x: f"{n} x {x} = {x*n}", range(1, 11)), sep="\n")


if __name__ == "__main__":
    n = int(input().strip())
    print_multiples(n)
