
#import pandas as pd
#import matplotlib.pyplot as plt


#ventas = {'Ventas' : [1500, 2500, 1800], 'Meses' : ['Enero', 'Febrero', 'Marzo'] }

#df = pd.DataFrame(ventas)

#df.plot(kind = 'barh', x = 'Meses' , y = 'Ventas', xlabel = "Meses", ylabel = "Ventas")

#plt.show()

#EJERCICIO 1

import pandas as pd
import matplotlib.pyplot as plt

def graficarGuardar1(series, titulo):
    fig, ax = plt.subplots()
    series.plot(kind= 'pie', ax = ax)
    ax.set_title(titulo)
    #plt.title(titulo)
    plt.ylabel("")
    plt.savefig(titulo + '.png')
    plt.show()
def graficarGuardar2(series, titulo):
    series.plot(kind= 'pie', ylabel = "", title= titulo)
    plt.savefig(titulo + '.png') #GUARDA FIGURA
    plt.show()
    
ventas = {'Enero' : 1500, 'Febrero' : 2500, 'Marzo' : 1800 }
series = pd.Series(ventas)
graficarGuardar1(series, 'ventas de un producto durante los meses de un trimestre')
