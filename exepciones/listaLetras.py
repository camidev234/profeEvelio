
listado=[]
def llenarLista(lista=listado):
    print("Escriba Uno para dejar de agregar elementos..")
    while True:
        p = input("Escriba la letra que desa agregar: ")
        elemento = p.upper()
        if p == "1":
            return True
        else:
            try:
                if len(elemento) > 1:
                    raise ValueError("El elemento ingresado no es valido.")
                else:
                    if elemento in lista:
                        raise ValueError(f"El elemento {p} ya esta en la lista")
                    else: lista.append(elemento)
            except Exception as p:
                print("error: ", p)
def mostrarLista():
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
            print(mostrarLista())
        case 3:
            buscarElemento()
        case 0:
            break        
