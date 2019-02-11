import numpy as np
import matplotlib.pyplot as plt
from mendeleev import element

mc2_e_MeV = 0.511
mc2_p_MeV = 938.27
mc2_n_MeV = 939.57
mc2_h_MeV = 938.78

mc2_e_amu = .0005488
mc2_p_amu = 1.007276
mc2_n_amu = 1.008665
mc2_h_amu = 1.007825


def nuclear_mass(A, Z):
    return get_element(A, Z).mass - (Z*mc2_e_amu)


def binding_energy(elem):

    Z = elem.atomic_number
    N = get_neutrons(elem)

    neutrons_mass  = N * mc2_n_amu
    hydrogens_mass = Z * mc2_h_amu
    atomic_mass    = elem.mass

    energy_binding = neutrons_mass + hydrogens_mass - atomic_mass

    return energy_binding


def get_element(A, Z):
    #if A != Z :
    #    N = A - Z
    #    return element(Z).isotopes.filter(Isotope.Z==3)
    return element(Z)


def get_neutrons(elem):
    return int(round(elem.mass)) - elem.atomic_number


def amu_to_MeV(x):
    return x * 931.5


x = [element(i).isotopes for i in range(1, 118)]
# ridiculous list comprehension that flattens  the list of lists of isotopes and removes those without a mass value
s = [n for i in x for n in i if n.mass is not None]


a = np.array([i.mass for i in s])
y = np.array([amu_to_MeV(binding_energy(i)) for i in s])
y = y/a


plt.scatter(a, y)
plt.xlabel("A")
plt.ylabel("Nuclear Binding Energy / Nucleon (A)")
plt.title("Per Nucleon Binding Energy (PNBE) by Number of Nucleons")
plt.show()
