class Contacto:
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        
    
    def getNombre(self):
        return self.__nombre
    
    def getTelefono(self):
        return self.__telefono
    
    def getEmail(self):
        return self.__email
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setTelefono(self, telefono):
        self.__telefono = telefono
        
    def setEmail(self, email):
        self.__email = email