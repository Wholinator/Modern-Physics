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


#H = (element('H'))
#print(H.isotopes[1].mass * 931.5)

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


ni_62 = element(28).isotopes[3]
print(amu_to_MeV(binding_energy(ni_62)) / ni_62.mass)

#ne = element(10).isoto

for i in element(10).isotopes:
    print(i.mass)

x = [i for i in range(1,100)]
a = [element(i).isotopes[0].mass for i in x]
y = [amu_to_MeV(binding_energy(element(i).isotopes[0])) / a[i-1] for i in x]


plt.scatter(a, y)
plt.show()
