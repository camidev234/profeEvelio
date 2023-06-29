from Agenda import *
from conexion import *
from Contacto import *

print("""
1. Crear nuevo contacto
2. Eliminar contacto
3. Actualizar nombre contacto
4. Actualizar Telefono contacto.
5. Actualizar email contacto
6. Actualizar contacto por completo       
7 Salir 
      
""")

while True:
    opc = int(input("Escoja la opcion de su preferencia: "))
    match opc:
        case 1: 
            n = input("Nombre del contecto: ")
            t = int(input("Telefono del contacto: "))
            e = input("Email del contacto: ")
            contactoNuevo = Contacto(n,t,e)
            Agenda.agregarContacto(contactoNuevo)
        case 2:
            cursor.execute("SELECT * FROM contactos")
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"id: {i[0]} nombre: {i[1]} telefono: {i[2]}")
            id = int(input("Escriba el id del contacto que desea eliminar: "))
            Agenda.eliminarContacto(id)
        case 3:
            cursor.execute("SELECT * FROM contactos")
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"id: {i[0]} nombre: {i[1]} telefono: {i[2]}")
            id = int(input("Escriba el id del contacto que desea actualizar: "))
            nombre = input("Escriba el nuevo nombre del contacto.")
            Agenda.modificarNombreContacto(id, nombre)
        case 4:
            cursor.execute("SELECT * FROM contactos")
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"id: {i[0]} nombre: {i[1]} telefono: {i[2]}")
            id = int(input("Escriba el id del contacto que desea actualizar: "))  
            telefono = int(input("Escriba el nuevo telefono del contacto: "))
            Agenda.modificarTelefonoContacto(id, telefono)  
        case 5:
            cursor.execute("SELECT * FROM contactos")
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"id: {i[0]} nombre: {i[1]} telefono: {i[2]}")
            id = int(input("Escriba el id del contacto que desea actualizar: "))
            email = input("Escriba el nuevo email del contacto: ")
            Agenda.modificarCorreoContacto(id, email)
        case 6:
            cursor.execute("SELECT * FROM contactos")
            resultado = cursor.fetchall()
            for i in resultado:
                print(f"id: {i[0]} nombre: {i[1]} telefono: {i[2]}")
            id = int(input("Escriba el id del contacto que desea actualizar: "))
            nombre = input("Escriba el nuevo nombre del contacto: ")
            telefono = int(input("Escriba el nuevo telefono del contacto: "))
            email = input("Escriba el nuevo email del contacto: ") 
            Agenda.modificarContacto(nombre, telefono, email, id)
        case 7:
            break