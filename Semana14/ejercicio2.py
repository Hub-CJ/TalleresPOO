
import pandas as pd
import matplotlib.pyplot as plt

def graficoVentas(sventas, tipoGrafico):
    fig, ax = plt.subplots()
    sventas.plot(kind = tipoGrafico, ax = ax, xlabel = 'Anios', ylabel = 'Ventas', title = 'Evolucion del numero de ventas')
    return ax

series = pd.Series([158, 128, 147, 195], index = [2022, 2021, 2020, 2019])
print(series)
graficoVentas(series, 'bar')
plt.show()
graficoVentas(series, 'barh')
plt.show()
graficoVentas(series, 'pie')
plt.show()
graficoVentas(series, 'line')
plt.show()
graficoVentas(series, 'area')
plt.show()
