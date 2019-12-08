# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:45:01 2019

@author: jomitame
"""
# Plantilla de pre-procesado - Datos Faltantes

# importando libreria
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importando el dataset
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# Tratamiento de los NAs
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="mean")
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])