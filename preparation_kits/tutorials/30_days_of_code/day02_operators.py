# Day 2: Operators #################################################################################################################

# Objective ###
# In this challenge, you will work with arithmetic operators.

# Task ###
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
# and tax percent (the percentage of the meal price being added as tax) for a meal,
# find and print the meal's total cost. Round the result to the nearest integer.

# Function Description ###
# Complete the solve function in the editor below.
# solve has the following parameters:
# - int meal_cost: the cost of food before tip and tax
# - int tip_percent: the tip percentage
# - int tax_percent: the tax percentage
# Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

# Input Format ###
# There are 3 lines of numeric input:
# The first line has a double, meal_cost (the cost of the meal before tax and tip).
# The second line has an integer, tip_percent (the percentage of meal_cost being added as tip).
# The third line has an integer, tax_percent (the percentage of meal_cost being added as tax).

# CODE #############################################################################################################################

# #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'solve' function below.
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent


def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    total_cost = meal_cost * (1 + (tip_percent / 100) + (tax_percent / 100))
    print(round(total_cost))


if __name__ == "__main__":
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
