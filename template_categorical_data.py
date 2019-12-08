# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:44:09 2019

@author: jomitame
"""
# Plantilla de pre-procesado - Datos Categóricos

# importando libreria
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importando el dataset
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# Codificando los datos categóricos (los de texto)
from sklearn import preprocessing
le_X = preprocessing.LabelEncoder()
X[:,0] = le_X.fit_transform(X[:,0])
onehotencoder = preprocessing.OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
le_y = preprocessing.LabelEncoder()
y = le_y.fit_transform(y)