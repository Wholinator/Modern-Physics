import numpy as np
from time import perf_counter_ns
from Relativity import Relativistic_Graphing as Graph
from Relativity import Classical_Transforms as Classical
from Relativity import Relativistic_Transforms as Relative

# speed of light
c = Relative.c

# list of objects
observers = []


class Observer:
    def __init__(self, x_i, y_i, m0, t_i=0., vx_i=0., vy_i=0., ax_i=0., ay_i=0., fx_i=0., fy_i=0.):
        self.x = x_i
        self.y = y_i

        self.t = t_i
        self.m0 = m0

        self.vx = vx_i
        self.vy = vy_i

        self.ax = ax_i
        self.ay = ay_i

        self.fx = fx_i
        self.fy = fy_i

        self.r = (np.sqrt(m0) / np.sqrt(np.pi)) / 2


# TODO: vectorize or figure out tensors
def tick(dt, obs_list):

    dt = dt * 10**-9

    for observer in obs_list:

        fx_i = 100
        fy_i = 0

        ax_new = Relative.force_to_acceleration(observer.m0, fx_i, observer.vx)
        ay_new = Relative.force_to_acceleration(observer.m0, fy_i, observer.vy)

        # verlet scheme
        observer.x = observer.x + (observer.vx * dt) + ((1 / 2) * observer.ax * dt**2)
        observer.y = observer.y + (observer.vy * dt) + ((1 / 2) * observer.ay * dt**2)

        observer.vx = observer.vx + ((1/2) * (ax_new + observer.ax) * dt)
        observer.vy = observer.vy + ((1/2) * (ay_new + observer.ay) * dt)

        observer.ax = ax_new
        observer.ay = ay_new

        Graph.paint(obs_list)


Graph.__init__()

observers.append(Observer(10., 10., 10))
observers.append(Observer(20., 30., 100))

t = perf_counter_ns()

while True:
    t_ = perf_counter_ns()

    tick(t_ - t, observers)

    t = t_
