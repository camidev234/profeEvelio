from Cuenta import *

class CuentaCorriente(Cuenta):
    def __init__(self, numero, saldo):
        Cuenta.__init__(self, numero, saldo)