
#lista = [18, 19, 1, 6, 8, 7, 3, 9, 15, 18]
#print(lista[1:8:2])
#lista[1:8:2] = [1, 2, 3, 4]
#print(lista)

import random as r 
def generar(n):
    lista = []
    for i in range(n):
        lista.append(chr(r.randint(65, 90)))
    return lista

def esVocal(letra):
    return letra in 'AEIOU'

def analizarAlternoAscendente(caracteres):
    for i in range(len(caracteres) - 6):
       if (esVocal(caracteres[i]) and esVocal(caracteres[i + 2]) and esVocal(caracteres[i + 4]) 
        and esVocal(caracteres[i + 6]) and caracteres[i] < caracteres[i + 2] and 
        caracteres[i + 2] < caracteres[i + 4] and caracteres[i + 4] < caracteres[i + 6]):
           print("Se encontro 4 vocales alternas y ascendentes")
def ordenarPosicionImpar(caracteres):
    print(caracteres)
    caracteres[1::2] = sorted(caracteres[1::2], reverse = True)
    print(caracteres)
n = -1
while not(n > 0 and n <= 50):
    n = int(input("Ingrese n : "))

caracteres = generar(n)
analizarAlternoAscendente(caracteres)
ordenarPosicionImpar(caracteres)

