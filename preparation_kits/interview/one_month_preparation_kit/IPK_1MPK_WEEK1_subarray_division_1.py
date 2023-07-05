# Subarray Division 1 ################################################################################################################################################

# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
#   - The length of the segment matches Ron's birth month, and,
#   - The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

# Function Description ###
# Complete the birthday function in the editor below.
# birthday has the following parameter(s):
#   - int s[n]: the numbers on each of the squares of chocolate
#   - int d: Ron's birth day
#   - int m: Ron's birth month
# Returns
#   - int: the number of ways the bar can be divided

# Input Format ###
# The first line contains an integer n, the number of squares in the chocolate bar.
# The second line contains n space-separated integers s[i], the numbers on the chocolate squares where 0 <= i <= n.
# The third line contains two space-separated integers, d and m, Ron's birth day and his birth month.

# CODE ###############################################################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s, d, m):
    # Write your code here
    res = [sum(s[i : i + m]) == d for i in range(0, len(s)) if i + m <= len(s)]
    return res.count(True)


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(f"{result}\n")

    # fptr.write(str(result) + "\n")

    # fptr.close()
