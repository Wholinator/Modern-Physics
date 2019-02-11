import numpy as np
import matplotlib as plt
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


def binding_energy(Z):
    A=0
    elem = get_element(A, Z)
    N = A - Z

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


def amu_to_MeV(x):
    return x * 931.5

print(amu_to_MeV(binding_energy(3)))