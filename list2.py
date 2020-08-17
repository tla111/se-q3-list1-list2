#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie assignment: List2
"""
# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Timothy La (tla111), Received help from Joseph"

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# D. remove_adjacent
# Given a list of numbers, return a list where all adjacent
# equal elements have been reduced to a single element.
# Example:
#   [1, 2, 2, 3] -> [1, 2, 3]
# You may create a new list or modify the passed in list.
# Hint: Don't use set()


def remove_adjacent(nums):
    new_list = []
    # first_num = new_list.(nums[0])
    for x in nums:
        if len(new_list) == 0 or x != new_list[-1]:
            new_list.append(x)
    return new_list

# Check previous number, compare with newest item added in new list.

# Filter method

# E. zip_merge
# Given two lists, combine the values from their corresponding
# indices into a single list.
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# result = ['My', 'name', 'is', 'Kelly']
# Hint: Think of it as "zipping" two lists together.  Is there
# a built-in function in python that will do this?


def zip_merge(list1, list2):
    new_list = zip(list1, list2)
    zipped_list = list(new_list)
    converted_list = []
    for item, item2 in zipped_list:
        converted_list.append(item + item2)
    return converted_list


# F. empty_filter
# Given a single list containing strings, empty strings, and
# None values:  Return a new list with the same elements, but
# strip out (filter) the empty strings and None values away.
# example: list1 = ["Mike", "", "Emma", None, "Kelly", "", "Brad", None]
# result:  ["Mike", "Emma", "Kelly", "Brad"]
# Hint: There is a Python idiom for doing this.  Can you find it?


def empty_filter(list1):
    def no_empty_strings(name):
        if name == "" or name is None:
            return False
        else:
            return True
    list_of_names = filter(no_empty_strings, list1)
    return list(list_of_names)


# G. linear_merge
# Given two lists sorted in increasing order, create and
# return a merged list of all the elements in sorted order.
# You may modify the passed in lists.
# The solution should work in "linear" time, making a single
# pass of both lists.
# Hint: Don't use `sort` or `sorted` -- they are not O(n)
# linear time and the two lists are already provided in
# ascending sorted order.


def linear_merge(list1, list2):
    result_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] > list2[0]:
            remove_item_list2 = list2.pop(0)
            result_list.append(remove_item_list2)
        else:
            remove_item_list1 = list1.pop(0)
            result_list.append(remove_item_list1)
    result_list.extend(list1)
    result_list.extend(list2)
    return result_list


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(
        prefix,
        repr(got),
        repr(expected)))

# The main() function calls the above functions with interesting
# inputs, using test() to check whether each result is correct or not.


def main():
    # Each line calls one of the functions above and compares its
    # result to the expected return value for that call.
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    test(remove_adjacent([2, 2, 3, 3, 3, 4, 5, 2, 3]), [2, 3, 4, 5, 2, 3])

    print('\nlinear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

    print('\nzip_merge')
    test(zip_merge(["M", "na", "i", "Ke"], ["y", "me", "s", "lly"]),
         ['My', 'name', 'is', 'Kelly'])

    print('\nempty_filter')
    test(empty_filter(["Mike", "", "Emma", None, "Kelly", "", "Brad", None]),
         ["Mike", "Emma", "Kelly", "Brad"])


# Standard boilerplate (python idiom) to call the main() function.
# This is called an "import guard".
if __name__ == '__main__':
    main()
