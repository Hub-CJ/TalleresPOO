from CuentaCorriente  import CuentaCorriente
import pandas as pd

def mostrarInformacion(cuentas):
    for i in cuentas:
        print(i.consultarCuenta())

df = pd.read_csv("MOCK_DATA.csv")
cuentas = []
for i in range(len(df)):
    cuenta = CuentaCorriente(df["id"][i], df["first_name"][i], df["last_name"][i], df["address"][i], df["phone"][i], float(df["money"][i]))
    cuentas.append(cuenta)
mostrarInformacion(cuentas)
dniRetiro = int(input("Ingrese el DNI del retiro : "))
dniDeposito = int(input("Ingrese el DNI del deposito : "))
monto = float(input("Ingrese el monto a transferir : "))
for i in cuentas:
    if(i.getDNI() == dniRetiro):
        i.retirarDinero(monto)
    if(i.getDNI() == dniDeposito):
        i.ingresarDinero(monto)
mostrarInformacion(cuentas)

distrito = input("Ingrese el distrito : ")
cont = sumatoria = 0
for i in cuentas:
    if(i.getDistrito() == distrito):
        cont+=1
        sumatoria+=i.getSaldo()
if cont == 0:
    print("No hay cuentas en el distrito ingresado")
else:
    print("El promedio de saldo es : ", sumatoria/cont)
inicial = input("Ingrese la inicial del apellido : ")    
for i in cuentas:
    if(i.getInicialApellido() == inicial):
        print(i.consultarCuenta())
print("Personas con mayor saldo")
mayorSaldo = cuentas[0].getSaldo()
for i in cuentas:
    if i.getSaldo() > mayorSaldo:
        mayorSaldo = i.getSaldo()
for i in cuentas:
    if i.getSaldo() == mayorSaldo:
       print(i.consultarCuenta())