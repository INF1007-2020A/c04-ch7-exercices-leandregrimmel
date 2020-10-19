#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from turtle import *


# TODO: Définissez vos fonction ici
def volumeEllipsoide(a, b, c, masse_volumique):
    volume = 4 / 3 * math.pi * a * b * c
    masse = masse_volumique * volume
    my_tuple = (volume, masse)

    return my_tuple


def drawTree():
    setheading(90)
    color('green')

    drawBranch()
    done()


def drawBranch(branch_len=70, pen_size=7, angle=35):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        drawBranch(branch_len - 10, pen_size - 1, angle - 5)
        left(2*angle)
        drawBranch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volumeEllipsoide(2, 4, 2, 10))
    # print((lambda sentence: sorted(frequence(sentence)), key = frequence(sentence).__getitem__)[-1])("Ceci est une phrase")

    # print (frequence("phrases"))
    drawTree()
