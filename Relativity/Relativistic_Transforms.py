###
### Relativistic definitions of Physical Transformations
###

import numpy as np

c = 299792458


def vel_add(v, u):
    return (v + u) / (1 + (v*u)/(c**2))

def time_dilation(t_0, u):
    return t_0 * gamma(u)

def length_contraction(l_0, u):
    return l_0 / gamma(u)

def gamma(u):
    return 1 / np.sqrt(1 - (u/c)**2)