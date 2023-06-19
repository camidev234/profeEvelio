class Cuenta:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        
    def getNumero(self):
        return self.__numero
    
    
    def getSaldo(self):
        return self.__saldo