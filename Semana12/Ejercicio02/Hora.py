class Hora:
    def __init__(self, hora, minuto, segundo):
        if hora < 0 or hora > 23:
            self.__hora = 0
        else:
            self.__hora = hora
        if minuto < 0 or minuto > 59: 
            self.__minuto = 0
        else:
            self.__minuto = minuto;
        if segundo < 0 or segundo > 59: 
            self.__segundo = 0
        else:
            self.__segundo = segundo
    #def __init__(self):
    #    self.__hora = 0;
    #    self.__minuto = 0;
    #    self.__segundo = 0;
    def setHoraMinutoSegundo(self, hora, minuto, segundo):
        if hora < 0 or hora > 23:
            self.__hora = 0
        else:
            self.__hora = hora
        if minuto < 0 or minuto > 59: 
            self.__minuto = 0
        else:
            self.__minuto = minuto;
        if segundo < 0 or segundo > 59: 
            self.__segundo = 0
        else:
            self.__segundo = segundo
    def getHora(self):
        return [self.__hora, self.__minuto, self.__segundo]
    def imprimirHora(self):
        print("{} : {} : {}".format(self.__hora, self.__minuto, self.__segundo))
    def getHora(self):
        return self.__hora
    def getMinuto(self):
        return self.__minuto
    def getSegundo(self):
        return self.__segundo
    def setHora(self, hora):
        self.__hora = hora
    def setMinuto(self, minuto):
        self.__minuto = minuto
    def setSegundo(self, segundo):
        self.__segundo = segundo
    def segundosTotales(self):
        return self.__hora * 3600+ self.__minuto * 60 + self.__segundo
    def incrementarSegundo(self):
        segundos = self.segundosTotales() + 1
        self.__hora = segundos // 3600
        segundos = segundos % 3600
        self.__minuto = segundos // 60
        self.__segundo = segundos % 60
        if self.__hora > 23:
           self.__hora = 0
    def tiempoFaltanteFinalDia(self):
        restante = 24*3600 - self.segundosTotales()
        hora = restante // 3600
        restante = restante % 3600
        minuto = restante // 60
        segundo = restante % 60
        print(f"{hora} : {minuto} : {segundo}")

        
