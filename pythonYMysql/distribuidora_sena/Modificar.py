from conexion import *

# modificando datos de un cliente

def actualizarNombres():
    try:
        identificacion = int(input("Escriba la identificacion: "))
    except ValueError:
        print("Solo se admiten numeros.")
    nombres = input("Escriba los nuevos nombres: ")
    nom = nombres.upper()
    consulta = "UPDATE clientes SET nombres = %s WHERE id = %s"
    valores = (nom, identificacion)
    cursor.execute(consulta, valores)
    conn.commit()
    print("Actualizacion realizada con exito.")
    
def actualizarPrimerApellido():
    try:
        identificacion = int(input("Escriba la identificacion: "))
    except ValueError:
        print("Solo se admiten numeros.")
    primerApellido = input("Escriba el nuevo primer apellido: ")
    pa = primerApellido.upper()
    consulta = "UPDATE clientes SET primer_apellido = %s WHERE id = %s"
    valores = (pa, identificacion)
    cursor.execute(consulta, valores)
    conn.commit()
    print("Actualizacion realizada con exito.")
    
def actualizarCorreo():
    try:
        identificacion = int(input("Escriba la identificacion: "))
    except ValueError:
        print("Solo se admiten numeros.")
        
    correo = input("Escriba el nuevo correo: ")
    consulta = "UPDATE clientes SET correo = %s WHERE id = %s"
    valores = (correo, identificacion)
    cursor.execute(consulta, valores)
    conn.commit()
    print("Actualizacion realizada con exito.")
    
