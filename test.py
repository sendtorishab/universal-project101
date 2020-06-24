import numpy as nm
import scipy as scipy
import matplotlib as lib
import pandas as  pd
from scipy import integrate 
i=scipy.integrate.quad(lambda x:2*x,0,3)
print(i)
i2=scipy.integrate.quad(lambda x:3*x,0,3)
print(i2)
i3=scipy.integrate.quad(lambda x:4*x,0,3)
print(i3)
