from Cuenta import *

class CuentaAhorros(Cuenta):
    def __init__(self, numero, saldo):
        Cuenta.__init__(self, numero, saldo)
        
    