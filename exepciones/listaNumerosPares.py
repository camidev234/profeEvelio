listado = []

def llenarLista(lista= listado):
    print("Escriba Uno para dejar de agregar elementos..")
    while True:
        p = int(input("Escriba el elemento que desea agregar: "))
        if p==1:
            break
        if p % 2 == 0:
            lista.append(p)
        else:
            try:
                if p % 2 != 0:
                    raise ValueError("el numero no es un par.")
            except Exception as j:
                print("Error:", j)

def mostrarlista():
    return listado

def buscarElemento(l = listado):
    try:
        pos = int(input("ingrese la posición del elemento que desea obtener:"))
        listaIndices = []
        for i in range(len(l)):
            if i == pos:
                print(f"En la posición {pos}, el elemento es: {l[i]}")
            listaIndices+=[i]

        if pos not in listaIndices:
            raise IndexError(f"La posicion {pos} no existe en la lista")
    except ValueError:
        print(f"Lo que usted ingreso no es un valor valido.")
    except Exception as p:
        print(f"Error: {p}")

print("Escoga una de estas opciones: ")
print("1. Cargar una lista")
print("2. Mostrar lista")
print("3. bUSCAR EL CONTENIDO DE UNA POSICON")

while True:
    opcion = int(input("Escoja la opcion: "))


    match opcion:
        case 1:
            llenarLista()
        case 2:
            print(mostrarlista())
        case 3:
            buscarElemento()
        case 0:
            break  
