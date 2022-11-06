class Base:
    def __init__(self, dni, nombre, apellido, distrito, telefono, saldo):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._distrito = distrito
        self._telefono = telefono
        self._saldo = saldo
    def getDNI(self):
        return self._dni
    def getNombre(self):
        return self._nombre
    def getApellido(self):
        return self._apellido
    def getDistrito(self):
        return self._distrito
    def getTelefono(self):
        return self._telefono
    def getSaldo(self):
        return self._saldo
    def getInicialApellido(self):
        return self._apellido[0]
