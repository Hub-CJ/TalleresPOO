import pandas as pd
import os 

os.system("cls")


#a) Generar un DataFrame con los datos del archivo.
df = pd.read_csv("./Semana13/titanic.csv", index_col="PassengerId")
print(df)
#b) Mostrar las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus
#columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
print("Dimenciones ", df.shape) #Dimensiones
print("Numero de datos ",df.size) #Número de datos
print("Nombres de columnas ", df.columns) #Nombres de columnas
print("Nombres de filas ", df.index) #Nombres de filas
print(df.head(10)) #10 primeras filas
print(df.tail(10)) #10 últimas filas
print("Tipos de datos ", df.dtypes) #Tipos de datos
print("Informacion ", df.info())
#c) Mostrar los datos del pasajero con identificador 148.
print(df.loc[148])
print("Numero de fila 148")
print(df.iloc[148])
#d) Mostrar las filas pares del DataFrame.
print(df.iloc[1::2])
#e) Mostrar los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(df.Pclass == 1)
print(df[df.Pclass == 1].Name.sort_values())
#f) Mostrar el porcentaje de personas que sobrevivieron y murieron.
print(df.Survived.value_counts(normalize=True) * 100)
#g) Mostrar el porcentaje de personas que sobrevivieron en cada clase.
print(df.groupby("Pclass").Survived.value_counts(normalize=True) * 100)
#h) Eliminar del DataFrame los pasajeros con edad desconocida.
print(df.dropna(subset=["Age"])) #El dropna elimina los valores nulos
#i) Mostrar la edad promedio o media de las mujeres que viajaban en cada clase.
print(df.groupby(["Pclass", 'Sex']).Age.mean().unstack()["female"])
#j) Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df["Menor"] = df.Age < 18
#k) Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print(df.groupby(["Pclass", "Menor"]).Survived.value_counts(normalize=True) * 100)