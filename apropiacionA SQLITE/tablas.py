from conexion import *


cursor.execute("CREATE TABLE IF NOT EXISTS contactos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT(20) NOT NULL, telefono INTEGER(11) NOT NULL, email TEXT(50) NOT NULL)")
conexion.commit()