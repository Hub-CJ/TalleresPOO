from Base import Base
class CuentaCorriente(Base):
    def retirarDinero(self, monto):
        self._saldo -= monto # saldo = saldo - monto
    def ingresarDinero(self, monto):
        self._saldo += monto # saldo = saldo + monto
    def consultarCuenta(self):
        return "{} {} {} {} {} {}".format(self._dni, self._nombre, self._apellido, self._distrito, self._telefono, self._saldo)
    def saldoNegativo(self):
        return self._saldo < 0  