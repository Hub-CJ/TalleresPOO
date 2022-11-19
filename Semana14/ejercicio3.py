
import pandas as pd
import matplotlib.pyplot as plt

def retornarGrafico(dfventas):
    fig, ax = plt.subplots()
    dfventas.plot(ax =ax, title = 'Evolucion de ingresos y gastos')
    ax.set_ylim([0, max(dfventas['Ingresos'].max(), dfventas['Gastos'].max()) + 100])
    return ax


vetas = {'Ingresos' : [158, 123, 159, 158, 146], 'Saliros' : [0, 123, 42, 15, 48], 'Productos' : [168, 120, 10, 15, 134], 'Gastos' : [125, 158, 145, 162, 123], 'Meses' : ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'] }

dfvetas = pd.DataFrame(vetas).set_index('Meses')

print(dfvetas)

retornarGrafico(dfvetas)
plt.show()