import pandas as pd
import os

os.system("cls")
def evaluarCotizaciones(df):
    return pd.DataFrame([df.max(), df.min(), df.mean(), df.median()], index = ["max", "min", "mean", "median"])

df = pd.read_csv("./Semana13/cotizacion.csv", delimiter=";", decimal=",", thousands=".", encoding="latin-1", index_col="Nombre")
print(evaluarCotizaciones(df))