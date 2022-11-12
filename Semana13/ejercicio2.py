""" import pandas as pd
import os

os.system("cls")
def calcularBalance(df, meses):
    df["balance"] = df["ventas"] - df["gastos"]
    #print( df.set_index("meses").loc[meses, "balance"].sum())
    df = df.set_index("meses")
    return df.loc[meses, "balance"].sum()

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
ventas = [1256, 1200, 1034, 1456, 1567, 1456, 1456, 1456, 1456, 1456, 1456, 1456]
gastos = [1836, 158, 147, 198, 1657, 1457, 1457, 1457, 145, 13554, 1457, 1457]
df = pd.DataFrame({"meses": meses, "ventas": ventas, "gastos": gastos})

print(calcularBalance(df, ["enero", "diciembre"])) """

import pandas as pd
import os

os.system("cls")
def calcularBalance(df, datos):
    df["balance"] = df["ventas"] - df["gastos"]
    return df[df.meses.isin(datos)].balance.sum()


meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
ventas = [1256, 1200, 1034, 1456, 1567, 1456, 1456, 1456, 1456, 1456, 1456, 1456]
gastos = [1836, 158, 147, 198, 1657, 1457, 1457, 1457, 145, 13554, 1457, 1457]
df = pd.DataFrame({"meses": meses, "ventas": ventas, "gastos": gastos})

print(calcularBalance(df, ["enero", "diciembre", "julio"]))