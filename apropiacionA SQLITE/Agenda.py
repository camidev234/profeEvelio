import sqlite3
from conexion import *
from Contacto import *
class Agenda:
        
    @classmethod
    def agregarContacto(cls, contacto):
        sql = "INSERT INTO contactos (nombre, telefono, email) VALUES (?,?,?)"
        cursor.execute(sql, (contacto.getNombre(), contacto.getTelefono(), contacto.getEmail()))
        conexion.commit()
        print("Contacto agregado con exito")
    
    
    @classmethod 
    def eliminarContacto(cls, idContacto):
        sql = "DELETE FROM contactos WHERE id = ?"
        cursor.execute(sql, (idContacto,))
        conexion.commit()
        print(f"Contacto numero {idContacto} eliminado con exito")
        
    @classmethod
    def modificarNombreContacto(cls, idContacto, nombreNuevo):
        sql = "UPDATE contactos SET nombre = ? WHERE id = ?"
        cursor.execute(sql, (nombreNuevo, idContacto))
        conexion.commit()
        print("Nombre del contacto actualizado con exito")
        
    @classmethod
    def modificarTelefonoContacto(cls, idcon, telefonoNuevo):
        sql = "UPDATE contactos SET telefono = ? WHERE id = ?"
        cursor.execute(sql, (telefonoNuevo, idcon))
        conexion.commit()
        print("Telefono del contacto actualizado con exito")
        
    @classmethod
    def modificarCorreoContacto(cls, idcon, nuevoEmail):
        sql = "UPDATE contactos SET email = ? WHERE id = ?"
        cursor.execute(sql, (nuevoEmail, idcon))
        conexion.commit()
        print("Correo actualizado con exito")
        
    @classmethod
    def modificarContacto(cls, n, t, e, i):
        sql = "UPDATE contactos SET nombre = ?, telefono = ?, email = ? WHERE id = ?"
        cursor.execute(sql, (n, t, e, i))
        conexion.commit()
        print("Contacto actualizado con exito")