#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import sys

from numpy import key
sys.path.insert(1,r"/Users/leandregrimmel/Desktop/POLY/Intro. à la programmation (INF1007)/Pycharm Projects/Exercice/c04-ch6-exercices-leandregrimmel")
from exercise2 import frequence

# TODO: Définissez vos fonction ici
def volumeEllipsoide(a, b, c, masse_volumique):
    volume = 4 / 3 * pi * a * b * c
    masse = masse_volumique * volume
    my_tuple = (volume, masse)

    return my_tuple


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volumeEllipsoide(2, 4, 2, 10))
    print((lambda sentence: sorted(frequence(sentence)), key = frequence(sentence).__getitem__)[-1])("Ceci est une phrase")

    print (frequence("phrases"))