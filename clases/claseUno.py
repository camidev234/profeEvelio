class Persona:
    def __init__(self, id, codigo, nombre, direccion, telefono):
        self.__id = id
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def getInfo(self):
        return f"""
        Id: {self.getId()}
        codigo: {self.getCodigo()}
        nombre: {self.getNombre()}
        direccion: {self.getDireccion()}
        telefono: {self.gettelefono()}
        """

    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
        return self.__codigo
    
    def getId(self):
        return self.__id
    
    def getDireccion(self):
        return self.__direccion
    
    def gettelefono(self):
        return self.__telefono
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def setTelefono(self, telefono):
        self.__telefono = telefono
    
