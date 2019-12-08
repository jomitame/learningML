# -*- coding: utf-8 -*-
"""
Crated: 30-11-2019
author: jomitame
based-on: Machine learning udemy Juan Gimilla
"""

# Plantilla de pre-procesado

# importando libreria
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importando el dataset
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# Dividiendo el dataset en conjunto de entrenamiento y test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)


# Escalando de variables (Normalizandolos)
'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''
