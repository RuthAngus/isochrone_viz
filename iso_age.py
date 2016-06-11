import numpy as np
import matplotlib.pyplot as plt
from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones import StarModel

def iso_age(teff, logg, feh):
    dar = Dartmouth_Isochrone()
    mod = StarModel(dar, Teff=(teff, 80), Logg=(logg, 0.10), Feh=(feh, 0.1))
    logage, _, _ = mod.maxlike()
    age = np.exp(logage)
    return age

if __name__ == "__main__":
    calc_age(5778, 4.4, 0.)
