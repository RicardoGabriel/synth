"""
Created on Sun Feb  3 14:08:09 2019
@author: Ricardo Duque Gabriel

Code for the creation of a SCG for Australian GDP series  
using 34 OECD countries to be our donor pool
"""

import pandas as pd
from run import synth_tables


#import excel dataset to panda dataframe
df = pd.read_excel('Dataset_TermPaper.xlsx', header=0).iloc[:3360]

#define control units
control_units = list(set(df["code"]))
control_units.sort()
#leaving Australia out (code==AUS) 
control_units = control_units[1:]

#transform variables 'year' and 'quarter' to one integer time variable
#adjust in excel next time
x=1
for i in range(0,3360):
    df.year[i]=x
    x=x+1
    if x==97:
        x=1

df = df[df.gdp_s.notnull()]
df.drop(["unemp", "peg"], axis = 1, inplace = True) 

#define which predictors to use
predictors = [  "privcons_s", "govcons_s", "inv_s", "population", "debt"
             ]

#create synth tables
synth_tables(  df,
               predictors,
               "AUS",
               control_units,
               "code",
               "gdp_s",
               "year",
               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
               )

