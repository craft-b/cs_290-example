# Author: Bobby Craft
# Date: 2/17/2020
# Description: This file contains a Function that takes in a list of numbers and
# replaces each value in the list with it's squared value.


def square_list(list_of_nums):
    """Squares the numbers of the original list."""
    for num in range(len(list_of_nums)):
        list_of_nums[num] = list_of_nums[num]**2

