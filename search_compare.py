#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""search comparisons"""

from __future__ import division
import random
import timeit


def rand_list():
    """Generates a random list of numbers."""
    new_list = random.sample(range(1, 10000), 500)
    return new_list


def rand_list2():
    """Generates a random list of numbers and sorts them."""
    new_list2 = random.sample(range(1, 10000), 500)
    new_list2.sort()
    return new_list2


def sequential_search(a_list, item):
    """Searches a list for an item."""
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1
    return found


def ordered_sequential_search(a_list, item):
    """Searches a list for an item."""
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        if a_list[pos] > item:
            stop = True
        else:
            pos += 1
    return found


def binary_search_iterative(a_list, item):
    """Searches a list for an item."""
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        if item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found


def binary_search_recursive(a_list, item):
    """Searches a list for an item."""
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)


def test_search_func(test_to_run, test_name):
    """
    Args:
        test_to_run (var): The search test you want to run.
        test_name (str): the name of the search test you are running.
    Return:
        statement: states the average time if took to run the test 100
                   times, and the name of the test.
    Examples:
        >>> test_search(test1, 'Sequential')
        Sequential search took 0.0003986 seconds to run, on average.
    """

    result_list = []
    count = 100
    while count > 0:
        count -= 1
        result_list.append(test_to_run.timeit(number=1))
    avg = sum(result_list) / len(result_list)
    print "{} search took{:10.7f} seconds to run, on average.".format(test_name, avg)


if __name__ == "__main__":
    TEST1 = timeit.Timer("sequential_search(rand_list(), -1)",
                         "from __main__ import sequential_search, rand_list")
    TEST2 = timeit.Timer("ordered_sequential_search(rand_list2(), -1)",
                         "from __main__ import ordered_sequential_search, rand_list2")
    TEST3 = timeit.Timer("binary_search_iterative(rand_list2(), -1)",
                         "from __main__ import binary_search_iterative, rand_list2")
    TEST4 = timeit.Timer("binary_search_recursive(rand_list2(), -1)",
                         "from __main__ import binary_search_recursive, rand_list2")

    test_search_func(TEST1, 'Sequential')
    test_search_func(TEST2, 'Ordered Sequential')
    test_search_func(TEST3, 'Binary interative')
    test_search_func(TEST4, 'Binary recursive')
