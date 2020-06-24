import numpy as nm
import scipy as scipy
import matplotlib as lib
import pandas as  pd
from scipy import integrate 
i=scipy.integrate.quad(lambda x:2*x,0,3)
print(i)