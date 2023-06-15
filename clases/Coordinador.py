from Persona import *

class Coordinador(Persona):
    def __init__(self, fechaIngreso, dir_oficina, id, codigo, nombre, direccion, telefono):
        Persona.__init__(self, id, codigo,direccion, nombre, telefono)
        self._fechaIngreso = fechaIngreso
        self._dir_oficina = dir_oficina


    def get_Info(self):
       return f"""
       {Persona.getInfo(self)}
       Fecha Ingreso: {self._fechaIngreso}
       Direccion Oficina: {self._dir_oficina}
       """
    
    def getFechaIngreso(self):
        return self._fechaIngreso
    
    def setFechaIngreso(self, fechaIngreso):
        self._fechaIngreso = fechaIngreso

    def get_direccion(self):
        return self._dir_oficina
    
    def setDireccion(self, direccion):
        self._dir_oficina = direccion
        
