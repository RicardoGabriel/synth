"""
Created on Sun Feb  3 14:08:09 2019
@author: Ricardo Duque Gabriel

Code for the creation of a SCG for GDP series of the European Monetary Union 
Countries using countries outside the MU to be our donor pool
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from scipy.optimize import fmin_slsqp, minimize
import matplotlib.pyplot as plt

some_dataframe = pd.read_excel('Dataset_TermPaper.xlsx', header=1)