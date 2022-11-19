
import pandas as pd
import matplotlib.pyplot as plt

dfTitanic = pd.read_csv("titanic.csv")
print(dfTitanic)

fig, ax = plt.subplots()

#Grafico PIE de fallecidos y supervivientes
#df = dfTitanic['Survived'].value_counts() #DF con muertos y vivos
#print(df)
dfTitanic['Survived'].value_counts().plot(kind= "pie", ylabel = "", labels = ["Muertos", "Vivos"], title = "Cantidad de muertos y vivos", autopct ='%.2f%%')
plt.show()

#Histograma con las edades
dfTitanic['Age'].plot(kind = "hist", title = "Histograma de edades")
plt.show()


#Gráfico de barras con el número de personas en cada clase.
dfTitanic['Pclass'].value_counts().plot(kind= 'bar', title = 'Cantidad de personas en cada clase', xlabel = 'Clase', ylabel = 'Cantidad de personas')
plt.show()

#Gráfico de barras con el número de personas en cada clase.
dfTitanic.groupby('Pclass').size().plot(kind= 'bar', title = 'Cantidad de personas en cada clase', xlabel = 'Clase', ylabel = 'Cantidad de personas')
plt.show()

#Gráfico de barras con el número de personas fallecidas y supervivientes en cada clase.

print(dfTitanic.groupby(['Pclass', 'Survived']).size().unstack().plot(kind = "bar", title = "Numero de personas fallecidas y supervivientes en cada clase", xlabel = "Clase", ylabel = "Cantidad de personas"))
plt.show()

#Gráfico de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.

print(dfTitanic.groupby(['Pclass', 'Survived']).size().unstack().plot(kind = "bar", stacked = True, title = "Numero de personas fallecidas y supervivientes en cada clase", xlabel = "Clase", ylabel = "Cantidad de personas"))
plt.show()
