import pandas as pd
import os
os.system("cls")
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
ventas = [1256, 1200, 1034, 1456, 1567, 1456, 1456, 1456, 1456, 1456, 1456, 1456]
gastos = [1836, 158, 147, 198, 1657, 1457, 1457, 1457, 145, 13554, 1457, 1457]
df = pd.DataFrame({"meses": meses, "ventas": ventas, "gastos": gastos})
df.to_csv("./Semana13/ventas.csv", index = False)
print(df)
