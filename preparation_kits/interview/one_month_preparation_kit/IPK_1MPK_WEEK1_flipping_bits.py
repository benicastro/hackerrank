# Flipping Bits ######################################################################################################################################################

# You will be given a list of 32 bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1) and return the result as an unsigned integer.

# Function Description ###

# Complete the flippingBits function in the editor below.
# flippingBits has the following parameter(s):
#   - int n: an integer
# Returns
#   - int: the unsigned decimal integer result

# Input Format ###

# The first line of the input contains q, the number of queries.
# Each of the next q lines contain an integer, n, to process.

# CODE ##############################################################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    # Write your code here
    # return ~n + 2**32
    bits_rep = f"{n:032b}"
    res = "".join(["0" if i == "1" else "1" for i in bits_rep])
    return int(res, 2)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        print(str(result) + "\n")

        # fptr.write(str(result) + '\n')

    # fptr.close()
