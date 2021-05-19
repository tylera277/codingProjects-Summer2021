import numpy as np
import math


def v2f(v1i,v2i,m1,m2):

    a = m1*m2+m2**2.0
    b = -2*m1*m2*v1i - 2*(m2**2.0)*v2i
    c = 2*m1*m2*v1i*v2i + m2**2.0*v2i**2.0 - m1*m2*v2i**2.0

    quadTop = -b + math.sqrt(b**2.0 - 4*a*c)
    quadBot = 2*a

    return quadTop/quadBot


def v1f(v1i,v2i,v2ff,m1,m2):
    top = m1*v1i + m2*v2i - m2*v2ff

    return top/m1