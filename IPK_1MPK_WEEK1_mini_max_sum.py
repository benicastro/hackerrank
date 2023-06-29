# Mini-Max Sum #####################################################################################################################

# Given five positive integers, find the minimum and maximum values that can be calculated by
# summing exactly four of the five integers. Then print the respective minimum and maximum values
# as a single line of two space-separated long integers.

# Function Description ###
# Complete the miniMaxSum function in the editor below.
# miniMaxSum has the following parameter(s):
#   - arr: an array of  integers

# Input Format
# A single line of five space-separated integers.

# Output Format
# Print two space-separated long integers denoting the respective minimum and maximum values that can be
# calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# CODE #############################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    max_sum = sum(arr[1:])
    min_sum = sum(arr[:-1])
    print(f"{min_sum} {max_sum}")


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
