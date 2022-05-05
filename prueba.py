import pandas as pd
import numpy as np
import os

file = open(r"INTRODUCCION A LAS ESTRUCTURAS Y MANEJO DE DATOS\Airbnb-Madrid\madrid-airbnb-listings-small.csv")
file = pd.DataFrame(file)
print(file)
