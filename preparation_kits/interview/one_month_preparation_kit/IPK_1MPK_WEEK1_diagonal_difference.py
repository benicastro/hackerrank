# Diagonal Difference ##############################################################################################################################################

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# Function description ###
# Complete the diagonalDifference function in the editor below.

# diagonalDifference takes the following parameter:
#   - int arr[n][m]: an array of integers
# Return
#   - int: the absolute diagonal difference

# Input Format ###
# The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

# Output Format ###
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

# CODE #############################################################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    arr_len = len(arr[0])
    ltr_diag_sum = 0
    rtl_diag_sum = 0
    for i in range(arr_len):
        ltr_diag_sum += arr[i][i]
        rtl_diag_sum += arr[i][-(i + 1)]
    abs_diff = abs(ltr_diag_sum - rtl_diag_sum)
    return abs_diff


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(str(result) + "\n")

    # fptr.write(str(result) + '\n')

    # fptr.close()
