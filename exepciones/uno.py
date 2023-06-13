"""def division (x, y):
  return x/y

try:
  divisor = int(input("ingrese divisor:"))
  dividendo = int(input("ingrese dividendo:"))
  print(division(divisor,dividendo))
except ZeroDivisionError:
  print("No es posible dividir por cero (0)")
except ValueError:
  print("Número ingresado no válido")
except:
  print("Error al dividir")
else:
  print("La división se pudo llevar a cabo")
finally:
  print("gracias por usar la función division()")"""

"""def division (x, y):
  return x/y

try:
  divisor = int(input("ingrese divisor:"))
  dividendo = int(input("ingrese dividendo:"))
  print(division(divisor,dividendo))
except Exception as pepito:
  print("Error ", pepito)"""

"""try:
  edad = int (input("Ingrese su edad:"))
  if edad < 0:
    raise ValueError("La edad no puede ser negativa")
except Exception as e:
  print("Error ", e)
"""


"""for i in range(0, 50):
    try:
        if i == 0:
            raise ZeroDivisionError("No se puede tener el numero 0")
    except Exception as h:
        print(i, h)"""

"""

1. Finaliza el siguiente código con una gestión completa de sus excepciones.  El objetivo del programa es solicitar al usuario una posición de una lista y devolver el valor que se encuentra en dicha posición.  Prueba el programa enviando una posición inexistente y enviando una letra como posición.  El programa sólo terminará cuando se ejecute correctamente

"""

lista = [3,5,6,8,8,6,4,5,66,777,3,3,3,5,6,5]



try:
    pos = int(input("ingrese la posición del elemento que desea obtener:"))
    listaIndices = []
    for i in range(len(lista)):
        if i == pos:
            print(f"En la posición {pos}, el elemento es: {lista[i]}")
            listaIndices+=[i]

    if pos not in listaIndices:
        raise IndexError(f"La posicion {pos} no existe en la lista")
except ValueError:
    print(f"Lo que usted ingreso no es un valor valido.")
except Exception as p:
    print(f"Error: {p}")

