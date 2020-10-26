#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
# import math
# from turtle import *
#
#
# # TODO: Définissez vos fonction ici
# def volumeEllipsoide(a, b, c, masse_volumique):
#     volume = 4 / 3 * math.pi * a * b * c
#     masse = masse_volumique * volume
#     my_tuple = (volume, masse)
#
#     return my_tuple
#
#
# def drawTree():
#     setheading(90)
#     color('green')
#
#     drawBranch()
#     done()
#
#
# def drawBranch(branch_len=70, pen_size=7, angle=35):
#     if branch_len > 0 and pen_size > 0:
#         pensize(pen_size)
#         forward(branch_len)
#         right(angle)
#         drawBranch(branch_len - 10, pen_size - 1, angle - 5)
#         left(2 * angle)
#         drawBranch(branch_len - 10, pen_size - 1, angle - 5)
#         right(angle)
#         backward(branch_len)
#
# import math
from numpy import sort


def get_sorted_dict_by_decimals(dict_arg):
    sorted_dict = {}
    list = []
    for key in dict_arg:
        list.append(round(dict_arg[key] % 1, 5))

    sorted_list = sorted(list)

    for index in range(len(sorted_list)):
        for key in dict_arg:
            if sorted_list[index] == (round(dict_arg[key] % 1, 5)):
                sorted_dict[key] = dict_arg[key]

    return sorted_dict


if __name__ == '__main__':
    # # TODO: Appelez vos fonctions ici
    # print(volumeEllipsoide(2, 4, 2, 10))
    # # print((lambda sentence: sorted(frequence(sentence)), key = frequence(sentence).__getitem__)[-1])("Ceci est une phrase")
    #
    # # print (frequence("phrases"))
    # drawTree()

    data = {
        2: 2.1,
        3: 3.3,
        1: 1.4,
        4: 4.2
    }
    print(get_sorted_dict_by_decimals(data))
