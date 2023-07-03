# Time Conversion ####################################################################################################################################################

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Function Description ###
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
# timeConversion has the following parameter(s):
#   - string s: a time in  hour format
# Returns
#   - string: the time in  hour format

# Input Format ###
# A single string  that represents a time in qw-hour clock format (i.e.: hh:ss:mmAM  or hh:ss:mmPM).

# CODE ###############################################################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM":
        if s[:2] == "12":
            s_new = f"00{s[2:-2]}"
        else:
            s_new = s[:-2]
    else:
        if s[:2] == "12":
            s_new = s[:-2]
        else:
            s_new = f"{int(s[:2])+12}{s[2:-2]}"
    return s_new


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)
    print(result)

    # fptr.write(result + "\n")

    # fptr.close()
