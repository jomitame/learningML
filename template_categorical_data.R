# Plantilla para el pre procesado de datos - datos categoricos
# importando el dataset
dataset = read.csv("Data.csv")

# codificando variables cataegoricas
dataset$Country = factor(dataset$Country,
                         levels = c("France","Spain","Germany"),
                         labels = c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0,1))