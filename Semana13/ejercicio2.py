import pandas as pd
import os

os.system("cls")
def calcularBalance(df, meses):
    df["balance"] = df["ventas"] - df["gastos"]
    print(df)

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
ventas = [1256, 1200, 1034, 1456, 1567, 1456, 1456, 1456, 1456, 1456, 1456, 1456]
gastos = [1836, 158, 147, 198, 1657, 1457, 1457, 1457, 145, 13554, 1457, 1457]
df = pd.DataFrame({"meses": meses, "ventas": ventas, "gastos": gastos})

calcularBalance(df, ["enero", "febrero"])
