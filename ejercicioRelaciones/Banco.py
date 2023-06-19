from Cliente import *
class Banco:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__clientes = []
        self.__totalAhorros = 0
        self.__totalCorrientes = 0
        
    def adicionarCliente(self, cliente):
        self.__clientes+=[cliente]
        
    def obtener_numero_clientes(self):
        cont=0
        for i in self.__clientes:
            cont+=1
            
        return cont
    
    def obtenerClienteIndividual(self, numeroDocumento):
        clienteBuscado = 0
        for j in self.__clientes:
            if j.getCedula() == numeroDocumento:
                clienteBuscado = j
                print(f"Bienvenido {j.getNombre()}")
        return clienteBuscado
    
    def obtenerClientes(self):
        cont=0
        for i in self.__clientes:
            cont+=1
            print(f"""
            Cliente: {i.getNombre()}
            Cedula: {i.getCedula()}  
            """)
            
    def getNombre(self):
        return self.__nombre
    
    def getAhorros(self):
        return self.__totalAhorros
    
    def getCorrientes(self):
        return self.__totalCorrientes
    
    def setCorrientes(self, valor):
        self.__totalCorrientes+=valor
        
    def setAhorros(self, valor):
        self.__totalAhorros+=valor



listaOpc = []
def CrearBanco(o=1):
    contOpcUno = 0
    for h in range(len(listaOpc)):
        if listaOpc[h] == 1:
            contOpcUno +=1
    
    if contOpcUno > 1:
        print("Solo se puede crear un banco")
    else:
        nombre = input("Escroba el nombre del banco: ")
        banco = Banco(nombre)
        return banco
    
