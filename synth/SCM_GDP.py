"""
Created on Sun Feb  3 14:08:09 2019
@author: Ricardo Duque Gabriel

Code for the creation of a SCG for Australian GDP series  
using 32 OECD countries to be our donor pool
"""

#to do in the excel - exclude SVN and GRC from countries and compute gdp_s per
#capita and its lags (maybe)

import pandas as pd
from run import synth_tables

df = pd.read_pickle('123.pkl')

#define control units
control_units = list(set(df["code"]))
control_units.sort()
#leaving Australia out (code==AUS) 
control_units = control_units[1:32]


#define which predictors to use
predictors = ["gdp_s", "privcons_s"
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
               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
               )


#save the graph
#fig.savefig(ppj("OUT_FIGURES", "synthetic.png".format(model_name)))


#debugging
#foo=df
#treated_unit="AUS"
#index_variable="code"
#measured_variable="gdp_s"
#time_variable="year"
#predict_time=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#optimize_time=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#plot_time=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#function="mean"