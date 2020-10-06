#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi


# TODO: Définissez vos fonction ici
def volumeEllipsoide(a, b, c, masse_volumique):
    volume = 4 / 3 * pi * a * b * c
    masse = masse_volumique * volume
    my_tuple = (volume, masse)

    return my_tuple


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volumeEllipsoide(2, 4, 2, 10))
