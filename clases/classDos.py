from claseUno import *

class Instructor(Persona):
    def __init__(self, profesion, especicalidad, cargo, salario_basico, id, codigo, nombre, direccion, telefono):
        Persona.__init__(self, id, codigo, nombre, direccion, telefono)
        self.__profesion = profesion
        self.__especicalidad = especicalidad
        self.__cargo = cargo
        self.__salario_basico = salario_basico

    def get_Info(self):
        return f"""
        {Persona.getInfo(self)}
        Profesion: {self.__profesion}
        Especialidad: {self.__especicalidad}
        Cargo: {self.__cargo}
        Salario: {self.__salario_basico}
        """
    
    def get_profesion(self):
        return  self.__profesion
    def set_profesion(self, profesion):
        self.__profesion = profesion
    def get_especialidad(self):
        return self.__especicalidad
    def set_especialidad(self, especialidad):
        self.__especicalidad=especialidad
    def get_cargo(self):
        return self.__cargo 
    def set_cargo(self,cargo):
        self.__cargo= cargo
    def get_salario(self):
        return self.__salario_basico
    def set_salario(self, salario):
        self.__salario_basico = salario 
   
