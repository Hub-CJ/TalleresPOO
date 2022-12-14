import random as r 

class CEncuesta: 
    def __init__ (self):
        self.__edad = 0
        self.__sexo = 'F'
        self.__prueba = 'R'
        self.__satisfaccion = 'B'
    def __init__ (self, edad, sexo, prueba, satisfaccion):
        self.__edad = edad
        self.__sexo = sexo
        self.__prueba = prueba
        self.__satisfaccion = satisfaccion

    def getEdad(self) : 
        return self.__edad 
    def getSexo(self) :                                         
        return self.__sexo                                      
    def getPrueba(self) :                                       
        return self.__prueba                                    
    def getSatisfaccion(self) :                                 
       return self.__satisfaccion                               
                                                                
    def setEdad(self, edad ) :                                  
        self.__edad = edad                                     
    def setSexo(self, sexo) :                                  
        self.__sexo = sexo                                     
    def setPrueba(self, prueba) : 
        self.__prueba = prueba
    def setSatisfaccion(self, satisfaccion) :  
        self.__satisfaccion = satisfaccion

    def consultarEncuesta(self):
        print(f"{self.__edad}\t{self.__sexo}\t{self.__prueba}\t{self.__satisfaccion}")


def generar(n):
    lista = []
    auxsexo = ['F', 'M']
    auxprueba = ['R', 'H', 'C']
    auxsatisfaccion = ['R', 'B', 'M']
    for i in range(n):
        edad = r.randint(18, 75)
        sexo = auxsexo[r.randint(0, 1)]
        prueba = auxprueba[r.randint(0, 2)]
        satisfaccion = auxsatisfaccion[r.randint(0, 2)]
        lista.append(CEncuesta(edad, sexo, prueba, satisfaccion))
    return lista
def mostrar(encuestados):
    for persona in encuestados:
        persona.consultarEncuesta()

def determinarCantidadAdultosMayores(encuestados):
    cont = 0
    for persona in encuestados:
        if persona.getEdad() > 60:
            cont += 1
    print("Cantidad adultos mayores : ", cont)
def determinarPromedioEdadCovid(encuestados):
    sumEdad = cont =  0
    for persona in encuestados:
        if persona.getPrueba() == 'C' :
            sumEdad+= persona.getEdad()
            cont+=1
    print("Promedio de edades de personas que solicitaron prueba covid : ", (sumEdad / cont) if cont != 0 else 0)
def nivelesSatisfaccionConMayorFrecuencia(encuestados):
    cB = cR = cM = 0
    for persona in encuestados:
        if persona.getSatisfaccion() == 'B' :
            cB+=1
        elif persona.getSatisfaccion() == 'R' :
            cR+=1
        else:
            cM+=1
    print("Niveles con mayor satisfaccion : ")
    if cB >= cR and cB >= cM: 
        print("Bueno")
    if cR >= cB and cR >= cM: 
        print("Regular")
    if cM >= cR and cM >= cB: 
        print("Malo")
def determinarEdadMujerMasJoven(encuestados):
    minEdad = 100
    for persona in encuestados:
        if persona.getSexo() == 'F' and persona.getPrueba() != 'C':
            if minEdad > persona.getEdad():
                minEdad = persona.getEdad()
    if minEdad == 100:
        print("No se encontro mujer joven con las caracteristicas especificas")
    else:
        print("La minima edad de la mujer joven es : ", minEdad)

n = -1
while not(n > 0 and n <= 40):
    n = int(input("Ingrese n : "))
encuestados = generar(n)
mostrar(encuestados)
determinarCantidadAdultosMayores(encuestados)
determinarPromedioEdadCovid(encuestados)
nivelesSatisfaccionConMayorFrecuencia(encuestados)
determinarEdadMujerMasJoven(encuestados)
