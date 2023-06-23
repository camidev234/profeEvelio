# se importa el paquete mysql con el modulo connector
import mysql.connector
    
# se crea una conexion
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'distribuidora_sena'
)

# se crea el cursor para poder llevar a cabo las operaciones
cursor = conn.cursor()
#cerrando cursor
#  cursor.close()  
# cerrando la conexion  
# conn.close()