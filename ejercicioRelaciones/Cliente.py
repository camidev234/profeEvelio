from Cuenta import *
from Ahorros import *
from Corriente import *
import random
class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__saldoCuentaAhorros = 0
        self.__SaldoCuentaCorriente = 0
        self.numeroCuentaAhorros = 0
        self.numeroCuentaCorriente = 0
        
    def getNombre(self):
        return self.__nombre
    
    def getCedula(self):
        return self.__cedula
    
    def crearCuenta(self):
        saldo = 0
        
        print("1.Ahorros")
        print("2.Corriente")
        
        p = int(input("Escoja el tipo de cuenta: "))
        
        if p == 1:
            for o in range(5):
                o = random.randint(8,9)
                self.numeroCuentaAhorros+=o
                
            numero = self.numeroCuentaAhorros
            cuentaAhorros = CuentaAhorros(numero, saldo)
            print(f"Tu cuenta de ahorros fue creada con el numero: {self.numeroCuentaAhorros}")
        else:
            for j in range(9):
                j = random.randint(8,9)
                self.numeroCuentaCorriente+=j
            numero = self.numeroCuentaCorriente
            cuentaCorriente = CuentaCorriente(numero, saldo)
            print(f"Tu cuenta Corriente fue creada con el numero: {self.numeroCuentaCorriente}")

    def meterPlata(self, banco):
        print("1. Ahorros \n 2. Corriente")
        p = input("A que tipo de cuenta desea agregar dinero:")
        if p == "1":
            print(f"Cuenta de ahorros de {self.getNombre()} numero: {self.numeroCuentaAhorros}")
            valor = int(input("Cuanto vas a meter: "))
            self.__saldoCuentaAhorros+=valor
            banco.setAhorros(valor)
            return valor
        else:
            print(f"Cuenta Corriente de {self.getNombre()} numero: {self.numeroCuentaAhorros}")
            valor = int(input("Cuanto vas a meter: "))
            self.__SaldoCuentaCorriente+=valor
            banco.setCorrientes(valor)
            return valor
    def getSaldoCorriente(self):
        return self.__SaldoCuentaCorriente
    
    def getSaldoAhorros(self):
        return self.__saldoCuentaAhorros
            
        
        
    
    