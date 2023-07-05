# Permuting Two Arrays ###############################################################################################################################################

# There are two n-element arrays of integers, A and B. Permute them into some A' and B'
# such that the relation A'[i] + B'[i] >= k  holds for all i where 0 <= i < n.
# There will be q queries consisting of A, B, and k. For each query, return YES if some permutation A', B' satisfying the relation exists. Otherwise, return NO.

# Function Description ###

# Complete the twoArrays function in the editor below. It should return a string, either YES or NO.
# twoArrays has the following parameter(s):
#   - int k: an integer
#   - int A[n]: an array of integers
#   - int B[n]: an array of integers
# Returns
#   - string: either YES or NO

# Input Format ###
# The first line contains an integer q, the number of queries.
# The next q sets of 3 lines are as follows:
#   - The first line contains two space-separated integers n and k, the size of both arrays A and B, and the relation variable.
#   - The second line contains n space-separated integers A[i].
#   - The third line contains n space-separated integers B[i].

# CODE #############################################################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#


def twoArrays(k, A, B):
    # Write your code here
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        print(result + "\n")
        # fptr.write(result + '\n')

    # fptr.close()
