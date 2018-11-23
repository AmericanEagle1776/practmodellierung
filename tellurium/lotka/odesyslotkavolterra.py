import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

#ivs
sheep0 = 200
wolves0 = 50
y0 = [sheep0, wolves0]

#params in 1/day
a = 1
b = 0.1
c = 2


def f(t, y):
    sheepi, wolvesi = y

    sheep1 = a*sheepi - b * wolvesi * sheepi
    wolves1 = b * wolvesi * sheepi - c * wolvesi
    return [sheep1, wolves1]
