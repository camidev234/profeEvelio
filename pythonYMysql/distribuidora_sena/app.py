from conexion import *
from Insertar import *
from Modificar import *

# creando un menu para realizar las distintas operaciones

print("""
1.Crear nuevo cliente
2.Actualizar primer apellido cliente
3 Actualizar nombres cliente
4 Actualizar correo cliente
5 Salir
""")

while True:
    try:
        opcion = int(input("Escoja una opcion: "))
    except ValueError:
        print("No se admite ese valor")
    
    match opcion:
        case 1:
            insertarUsuario()
        case 2: 
            actualizarPrimerApellido()
        case 3:
            actualizarNombres()
        case 4:
            actualizarCorreo()
        case 5:
            break 
    
