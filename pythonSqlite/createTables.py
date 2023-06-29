from conexion import *


cursor.execute("CREATE TABLE IF NOT EXISTS persona (id INTEGER PRIMARY KEY AUTOINCREMENT, edad INTEGER NOT NULL, nombre TEXT NOT NULL)")