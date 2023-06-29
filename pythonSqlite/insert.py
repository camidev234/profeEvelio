from conexion import *

cursor.execute("INSERT INTO persona (edad, nombre) VALUES (17, 'Camilo Acevedo')")
cursor.execute("INSERT INTO persona (edad, nombre) VALUES (19, 'Camilo Beltran')")
cursor.execute("INSERT INTO persona (edad, nombre) VALUES (17, 'Yenny Beltran')")

conexion.commit()
