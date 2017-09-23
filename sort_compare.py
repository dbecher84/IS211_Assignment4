#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Runs time test on sort functions"""

from __future__ import division
import timeit
import random

def rand_list1():
    """Generates a random list of numbers."""
    new_list = random.sample(range(1, 20000), 500)
    return new_list

def rand_list2():
    """Generates a random list of numbers."""
    new_list = random.sample(range(1, 20000), 1000)
    return new_list

def rand_list3():
    """Generates a random list of numbers."""
    new_list = random.sample(range(1, 20000), 10000)
    return new_list

def insertion_sort(a_list):
    """Sorts a list of numbers."""
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

def shell_sort(a_list):
    """Sorts a list of numbers."""
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        #print("After increments of size", sublist_count, "The list is",a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    """Works with the shell_sort func to sort a list of numbers."""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

def python_sort(a_list):
    """Sorts a list of numbers."""
    a_list.sort()

def test_sort_func(test_to_run, test_description):
    """
    Args:
        test_to_run (var): The search test you want to run.
        test_name (str): the name of the search test you are running.
    Return:
        statement: states the average time if took to run the test, 100
                   times, and a desription of the test.
    Examples:
        >>> test_sort_func(TEST2, "Insertion Sort of 1000 items")
        Insertion Sort of 1000 items took 0.0516882 seconds to run, on average.
    """

    result_list = []
    count = 100
    while count > 0:
        count -= 1
        result_list.append(test_to_run.timeit(number=1))
    avg = sum(result_list) / len(result_list)
    print "{} took{:10.7f} seconds to run, on average.".format(test_description, avg)

if __name__ == "__main__":
    TEST1 = timeit.Timer("insertion_sort(rand_list1())",
                         "from __main__ import insertion_sort, rand_list1")
    TEST2 = timeit.Timer("insertion_sort(rand_list2())",
                         "from __main__ import insertion_sort, rand_list2")
    TEST3 = timeit.Timer("insertion_sort(rand_list3())",
                         "from __main__ import insertion_sort, rand_list3")
    TEST4 = timeit.Timer("shell_sort(rand_list1())",
                         "from __main__ import shell_sort, rand_list1")
    TEST5 = timeit.Timer("shell_sort(rand_list2())",
                         "from __main__ import shell_sort, rand_list2")
    TEST6 = timeit.Timer("shell_sort(rand_list3())",
                         "from __main__ import shell_sort, rand_list3")
    TEST7 = timeit.Timer("python_sort(rand_list1())",
                         "from __main__ import python_sort, rand_list1")
    TEST8 = timeit.Timer("python_sort(rand_list2())",
                         "from __main__ import python_sort, rand_list2")
    TEST9 = timeit.Timer("python_sort(rand_list3())",
                         "from __main__ import python_sort, rand_list3")

    test_sort_func(TEST1, "Insertion sort of 500 items")
    test_sort_func(TEST2, "Insertion sort of 1000 items")
    test_sort_func(TEST3, "Insertion sort of 10000 items")
    test_sort_func(TEST4, "Shell sort of 500 items")
    test_sort_func(TEST5, "Shell sort of 1000 items")
    test_sort_func(TEST6, "Shell sort of 10000 items")
    test_sort_func(TEST7, "Python sort of 500 items")
    test_sort_func(TEST8, "Python sort of 1000 items")
    test_sort_func(TEST9, "Python sort of 10000 items")
