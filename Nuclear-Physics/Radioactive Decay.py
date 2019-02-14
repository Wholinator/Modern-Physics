import numpy as np
import matplotlib as mt
import matplotlib.pyplot as plt
from mendeleev import element

def number_of_nuclei(N_0, decay, t):
    return N_0 * np.exp((-1) * decay * t)


decay = 0.5
N_0 = 50

t = [i for i in np.arange(0, 10, 0.1)]
y = [number_of_nuclei(N_0, decay, i) for i in t]


plt.plot(t, y)

plt.show()
