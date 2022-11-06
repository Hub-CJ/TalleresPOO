from Hora import Hora

def mostrar(horas):
    for hora in horas:
        hora.imprimirHora()

#hora, minuto, segundo = 0, 5, 0
hora =  minuto =  segundo = 0
horas = []
while hora != -1:
    hora = int(input("Ingrese hora : "))
    if hora != -1:
        minuto = int(input("Ingrese minuto : "))
        segundo = int(input("Ingrese segundo : "))
        objHora = Hora(hora, minuto, segundo)
        horas.append(objHora)
mostrar(horas)

for x in horas:
    x.incrementarSegundo()
mostrar(horas)
for x in horas:
    x.tiempoFaltanteFinalDia()
horaMayor = horas[0]
horaMenor = horas[0]
for x in horas: 
    if x.segundosTotales() > horaMayor.segundosTotales():
        horaMayor = x
    if x.segundosTotales() < horaMenor.segundosTotales():
        horaMenor = x
segundosTotales = horaMayor.segundosTotales() - horaMenor.segundosTotales()
print(f"{segundosTotales // 3600} : {(segundosTotales % 3600) // 60} : {((segundosTotales % 3600) % 60)}")
