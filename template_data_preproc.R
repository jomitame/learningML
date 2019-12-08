# Plantilla para el pre procesado de datos
# importando el dataset
dataset = read.csv("Data.csv")
#dataset = dataset[,2:3] # para algunos casos ????

# dividir los datos en conjuntos de entrenamiento y test
# debemos instalar caTools
# install.packages("caTools")
library(caTools)
# configurando semilla aleatoria
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# escalado de valores
# se escala de la columna 2 a la 3 porque la uno es texto y no numero
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])