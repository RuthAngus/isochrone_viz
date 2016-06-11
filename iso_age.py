import numpy as np
import matplotlib.pyplot as plt
from isochrones.dartmouth import Dartmouth_Isochrone
from isochrones import StarModel

def calc_age(data):
    return data
    dar = Dartmouth_Isochrone()
    mod = StarModel(dar, Teff=(5770, 80), logg=(4.44, 0.10), feh=(0.0, 0.1))
    logage, _, _ = mod.maxlike()
    age = np.exp(logage)
    print(age)
    return age

if __name__ == "__main__":
    calc_age(5778, 4.4, 0.)
