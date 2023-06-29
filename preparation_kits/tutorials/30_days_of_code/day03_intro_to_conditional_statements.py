# Day 03: Introduction to Conditional Statements ###################################################################################

# Objective ###
# In this challenge, we learn about conditional statements.

# Task ###
# Given an integer, N, perform the following conditional actions:

# If N is odd, print Weird
# If N is even and in the inclusive range of 2 to 5, print Not Weird
# If N is even and in the inclusive range of 6 to 20, print Weird
# If N is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

# Input Format ###
# A single line containing a positive integer, .

# Output Format ###
# Print Weird if the number is weird; otherwise, print Not Weird.

# CODE #############################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys


def check(N):
    ### This function evaluates the input N based on different conditions
    if N % 2 != 0:
        print("Weird")
    elif N > 20:
        print("Not Weird")
    elif N >= 6:
        print("Weird")
    else:
        print("Not Weird")


if __name__ == "__main__":
    N = int(input().strip())

    check(N)
