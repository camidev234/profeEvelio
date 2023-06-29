from conexion import *


cursor.execute("UPDATE persona SET nombre = 'Carlos Tello' WHERE id = 1")
conexion.commit()