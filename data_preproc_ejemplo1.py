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
# variable independiente se escribe en may´scula porque es una matriz
# se tomaron todas las filas con el primer dospuntos ":"}
# se tomaron todas las columnas excepto la última -1
# con .value se estipula que solo sean los valores y no las posiciones
X = dataset.iloc[:,:-1].values
# variable a predecir se escribe en minuscula por que es un vector
y = dataset.iloc[:,3].values

# Tratamiento de los NAs
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="mean")
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])

# Codificando los datos categóricos (los de texto)
from sklearn import preprocessing
le_X = preprocessing.LabelEncoder()
X[:,0] = le_X.fit_transform(X[:,0])
# variable dummy (coloca una columna por categoria 
# ya que NO es categoria ordinal como si lo son las tallas de la ropa)
onehotencoder = preprocessing.OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
# aqui SI es categoria ordinal
le_y = preprocessing.LabelEncoder()
y = le_y.fit_transform(y)

# Dividiendo el dataset en conjunto de entrenamiento y test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)

# Escalando de variables (Normalizandolos)
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
# los de X de test se escalaran con lo que detecte en X de train
X_test = sc_X.transform(X_test)

# no se hará el escalado en y porque es un algoritmo de CLASIFICACION y no de regresion "predicción"