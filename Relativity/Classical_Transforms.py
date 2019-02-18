#####################################################
# Classical Definitions of Physical Transformations #
#####################################################

import numpy as np

g = 6.67408 * (10**-11)


def vel_add(v, u):
    return v + u


def gravity(obs1, obs2):
    x = obs1.x - obs2.x
    y = obs1.y - obs2.y

    theta = np.arctan2(y, x)

    r = distance(obs1, obs2)

    g_mag = g * (obs1.mass * obs2.mass) / r**2

    return g_mag * np.cos(theta), g_mag * np.sin(theta)


def distance(obs1, obs2):
    return np.sqrt((obs1.x - obs2.x)**2 + (obs1.y - obs2.y)**2)
