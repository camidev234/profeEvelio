from conexion import *



# se crea la funcion insertarUsuario (insert)
# se deben incluir todos los campos de la tabla menos la columna auto incrementable
# def insertarUsuario(id, primerApellido, segundoApellido, nombres, email):
#     pa = primerApellido.upper()
#     sa = segundoApellido.upper()
#     nombre = nombres.upper()
#     # se realiza la consulta y en values se coloca el marcador de valores con %s
#     consulta = "INSERT INTO clientes (id, primer_apellido, segundo_apellido, nombres, correo) VALUES (%s, %s, %s, %s, %s)"
#     # en una variable se insertan los valores que va a tomar cada campo, en este caso es lo que se le pase como parametro a la funcion.
#     val = (id, pa, sa, nombre, email)
#     # se ejecuta la consulta especificando la misma y los valores
#     cursor.execute(consulta, val)
#     conn.commit()
#     print("Usuario creado con exito.")
# insertarUsuario(id, primer_apellido, segundo_apellido, nombres, email)
    
    
def insertarUsuario():
    id = int(input("Escriba el id del usuario: "))
    primer_apellido = input("Escriba el primer apellido: ")
    segundo_apellido = input("Escriba el segundo apellido: ")
    nombres = input("Escriba los nombres: ")
    email = input("Escriba el email: ")
    pa = primer_apellido.upper()
    sa = segundo_apellido.upper()
    nombre = nombres.upper()
    # se realiza la consulta y en values se coloca el marcador de valores con %s
    consulta = "INSERT INTO clientes (id, primer_apellido, segundo_apellido, nombres, correo) VALUES (%s, %s, %s, %s, %s)"
    # en una variable se insertan los valores que va a tomar cada campo, en este caso es lo que se le pase como parametro a la funcion.
    val = (id, pa, sa, nombre, email)
    # se ejecuta la consulta especificando la misma y los valores
    cursor.execute(consulta, val)
    conn.commit()
    print("Usuario creado con exito.")
    

