#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html

import random as r
import matplotlib.pyplot as plt
import pandas as pd
n = 15
gastos = []
ingresos = []
for i in range(n):
    gastos.append(r.randint(2000, 5000))
    ingresos.append(r.randint(2000, 5000))
print(gastos)
print(ingresos)
empresa = {
        "Gastos" : gastos, 
        "Ingresos": ingresos
    }
print(empresa)
df = pd.DataFrame(empresa)
print(df)
df.plot(kind = "line", title = "Evolucion de ingresos y gastos", ylim = (0))
plt.show()