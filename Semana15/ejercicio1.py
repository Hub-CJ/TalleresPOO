
def menu() :
    op = -1
    while not(op >= 1 and op <= 3):
        print("Menu de opciones     ")
        print("1. Calcular la serie ")
        print("2. Grafico           ")
        print("3. Fin               ")
        op = int(input("Ingrese opcion : "))
    return op

def calcularSerie(n, a):
    suma = 0
    for i in range(1, n + 1):
        suma += pow(-1, i +1 ) *(2 * i - 1) * pow(a, pow(2, i- 1)) / (2 * i)
    print("La suma es: ", suma)
def graficar(n):
    for fila in range(1, n + 1):
        cont = 1
        for esp in range(n - fila):
            print(" ", end = "")
        for colum in range(1, 2 * fila):
            print(cont, end = "")
            if colum < fila:
                cont +=1 
            else:
                cont -=1 
        print()
op = menu() 
while op != 3:
    if op == 1:
        n = -1
        while not(n > 0 and n < 21):
            n = int(input("Ingrese n : "))
        a = -1
        while not(a >= 0.5 and a <= 2):
            a = float(input("Ingrese a : "))
        calcularSerie(n, a)
    elif op == 2:
        n = -1
        while not(n > 0 and n < 10):
            n = int(input("Ingrese n : "))
        graficar(n)
    op = menu() 