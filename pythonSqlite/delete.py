from conexion import *


cursor.execute("DELETE FROM persona WHERE nombre = 'Carlos Tello'")

conexion.commit()