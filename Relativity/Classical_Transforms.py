#####################################################
# Classical Definitions of Physical Transformations #
#####################################################

import numpy as np

g = 6.67408 * (10**-11)


def vel_add(v, u):
    return v + u


def gravity(obs1, obs2):
    return g * (obs1.mass * obs2.mass) / distance(obs1, obs2)


def distance(obs1, obs2):
    return np.sqrt((obs1.x - obs2.x)**2 + (obs1.y - obs2.y)**2)
