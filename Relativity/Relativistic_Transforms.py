###
### Relativistic definitions of Physical Transformations
###

import numpy as np

c = 299792458
q_e = -1.6 * 10**-19


def gamma(u):
    if u == c:
        return float('inf')
    else:
        return 1 / np.sqrt(1 - (u/c)**2)


def time_dilation(t_0, u):
    return t_0 * gamma(u)


def length_contraction(l_0, u):
    return l_0 / gamma(u)


def vel_add(v, u):
    return (v + u) / (1 + (v*u)/(c**2))


# returns mass energy equivalence in eV
def mass_energy(m):
    return (m * c**2) / np.abs(q_e)


def k_energy(m, v):
    return mass_energy(m) * (gamma(v) - 1)


def total_energy(m, v):
    return mass_energy(m) * gamma(v)
