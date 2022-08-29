#!/usr/bin/python3
"""
function that divid a number by two
"""


def divisible_by_2(my_list=[]):

    new_list = []

    for i in range(len(my_list)):

        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
