# -*- coding: utf-8 -*-
"""
Processing the Comments on HOLC 
Taken from the geojson file
"""
import pandas as pd
import json
from pandas.io.json import json_normalize
data = pd.read_excel('C:/Users/jacar/OneDrive/Documents/Carnegie Mellon/Fall 2022/Telling Stories with Data/Final Project/Data/Comments Raw.xlsx')

dfls=[]
for row in range(len(data)):
    dictex = json.loads((data['Area Description Data'][row]))
    dfls.append(json_normalize(dictex))
dat2 = pd.concat(dfls)

dat3 = pd.concat([dat2.reset_index(drop=True), data['Holc Id']], axis=1)

# Casting variables of interest:
    # 4 : detrimental influences
    # 5.c : foreign born population
    # 5.d : Race
    # 5.b : Income
    # 14 : clarification
    # 5.e : income

data_for_exp = dat3[['Holc Id','1','4','5b','5c','5d','5e','14']]
data_for_exp.to_csv('C:/Users/jacar/OneDrive/Documents/Carnegie Mellon/Fall 2022/Telling Stories with Data/Final Project/Data/Processed File.csv')