import numpy
from numpy import sin, cos


# exe1
def sinx_x(x):
    if (x == 0):
        return 1
    return sin(x) / x


# exe2
def cosx_x(x):
    if (x == 0):
        return 1
    return cos(x) / x


# exe3
t = list()

for i in numpy.arange(-100.0, 100.0, 0.01):
    t.append(i)

print(t)

#exe4
sinx=[sinx_x(x) for x in t]

print(sinx)

#exe5
cosx=[cosx_x(x) for x in t]

print(cosx)
