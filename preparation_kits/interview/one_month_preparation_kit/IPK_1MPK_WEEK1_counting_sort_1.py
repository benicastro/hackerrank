# Counting Sort 1 ####################################################################################################################################################

# Comparison Sorting
# Quicksort usually has a running time of n x log(n), but is there an algorithm that can sort even faster? In general, this is not possible.
# Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm
# cannot beat n x log(n) (worst-case) running time, since n x log(n) represents the minimum number of comparisons needed to know where to place each element.

# Alternative Sorting
# Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values
# in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array,
# printing the value of each non-zero valued index that number of times.

# Challenge ###
# Given a list of integers, count and return the number of times each value appears as an array of integers.

# Function Description ###
# Complete the countingSort function in the editor below.
# countingSort has the following parameter(s):
#   - arr[n]: an array of integers
# Returns
#   - int[100]: a frequency array

# Input Format ###
# The first line contains an integer n, the number of items in arr.
# Each of the next n lines contains an integer arr[i] where 0 <= i < n.

# CODE ###############################################################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    arr_len = len(arr)
    res = [0] * 100
    for i in arr:
        res[i] += 1
    return res


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(" ".join(map(str, result)))
    print("\n")

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
