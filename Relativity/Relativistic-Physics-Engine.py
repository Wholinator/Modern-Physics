import numpy as np
import matplotlib.pyplot as plt
from Relativity import Classical_Transforms as Classical
from Relativity import Relativistic_Transforms as Relative


class Observer:
    def __init__(self, x_i, y_i, t_i, m0, vx_i=0, vy_i=0, a_i=0):
        self.x = x_i
        self.y = y_i
        self.t = t_i
        self.m0 = m0
        self.vx = vx_i
        self.vy = vy_i
        self.a = a_i


print(Relative.vel_add(10000, 10000))
print(Classical.vel_add(10000, 10000))
