########################################################
# Relativistic definitions of Physical Transformations #
########################################################

import numpy as np

c = 299792458

q_e = -1.6 * 10**-19
m_e = 9.11 * 10**-31
mc2_e_mev = 0.511

q_p = 1.6 * 10**-19
m_p = 1.67 * 10**-27
mc2_p_mev = 938.27


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


def momentum(m, v):
    return m * v * gamma(v)


# returns mass energy equivalence in eV
def mass_energy(m):
    return (m * c**2) / np.abs(q_e)


def k_energy(m, v):
    return mass_energy(m) * (gamma(v) - 1)


def total_energy(m, v):
    return mass_energy(m) * gamma(v)


# TODO: figure out the units, man
def force_to_acceleration(m, f, v):
    return f / (gamma(v)**3 * m)
