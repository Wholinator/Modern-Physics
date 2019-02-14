import numpy as np
import matplotlib.pyplot as plt
from mendeleev import element

x = [element(i).isotopes for i in range(1, 118)]
s = [n for i in x for n in i if n.mass is not None]

protons = [t.atomic_number for t in s]
neutrons = [t.mass_number - t.atomic_number for t in s]

# plots proton number by neutron number
plt.scatter(neutrons, protons, s=1, c='Black')

# plots simple y = x for comparison
plt.plot(np.arange(0, 125), np.arange(0, 125), c=(0.9, 0.2, 0.25, 1))

plt.show()
