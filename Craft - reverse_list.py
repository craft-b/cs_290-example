# Author: Bobby Craft
# Date: 2/18/2020
# Description: This file contains a Function that takes in a list of elements
# and reverses the order of the elements in the list.


def reverse_list(given_list):
    """Reverses the order of elements in the given list."""
    given_list[:] = given_list[::-1]
