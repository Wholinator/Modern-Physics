import numpy as np
import matplotlib.pyplot as plt
from Relativity import Relativistic_Graphing as Graph
from Relativity import Classical_Transforms as Classical
from Relativity import Relativistic_Transforms as Relative

c = Relative.c


class Observer:
    def __init__(self, x_i, y_i, t_i, m0, vx_i=0, vy_i=0, ax_i=0, ay_i=0):
        self.x = x_i
        self.y = y_i
        self.t = t_i
        self.m0 = m0
        self.vx = vx_i
        self.vy = vy_i
        self.ax = ax_i
        self.ay = ay_i


def tick(delta_t, obs_list):
    for observer in obs_list:

        # verlet scheme
        observer.x = observer.x + (observer.vx * delta_t) + ((1 / 2) * observer.ax * delta_t**2)
        observer.y = observer.y + (observer.vy * delta_t) + ((1 / 2) * observer.ay * delta_t**2)



print(Relative.k_energy(1.67*10**-27, c * 0.99999999999999999999999999))
