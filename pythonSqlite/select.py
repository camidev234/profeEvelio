from conexion import *

# visualizando todos los datos de la tabla persona
cursor.execute("SELECT * FROM persona")

# introduciendo los datos en una lista
result = cursor.fetchall()

print()
for r in result:
    print(f"Nombre: {r[2]} edad: {r[1]}")
    
print()

# retornando solo de un campo en especifico
cursor.execute("SELECT edad, nombre FROM persona WHERE id = 3")

# rsultado = cursor.fetchall()

# print(rsultado)

# for i in rsultado:
#     print(f"Nombre: {i[1]} Edad: {i[0]}")

res = cursor.fetchone()

print(res)


for h in res:
    print(f"edad: {r[1]} nombre: {r[2]}")


