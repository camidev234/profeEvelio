from Cliente import *
from Banco import *
from Cuenta import *
from Ahorros import *
from Corriente import *

print("Escoja una de las siguientes opciones: ")
print("""  
1. Crear Banco
2. Agregar Cliente a un Banco
3. Ver los clientes de un Banco
4. Obtener el número de clientes de un Banco
5. Crear Cuenta
6. Meter Plata
7. Ver totales Ahorros Banco
8. Ver totales Corrientes Banco
9. Ver totales ahorros Cliente
10. ver totales Corrientes Cliente
11. Salir
""") 
contVecesSiete=0
contVecesOcho = 0
while True:
    opcion = int(input("Escriba la opcion de su preferencia: "))
    listaOpc.append(opcion)
    match opcion:
        case 1:
            b = CrearBanco()
        case 2:
            if 1 not in listaOpc:
                print("Debes haber creado un banco.")
            else:
                nombre = input("Escriba el nombre del cliente: ")
                documento = int(input(f"Escriba el numero de documento de {nombre}: "))
                cliente = Cliente(nombre, documento)
                b.adicionarCliente(cliente)
        case 11:
            break
        case 3:
            b.obtenerClientes()
        case 4:
            print(f"El numero de clientes del banco {b.getNombre()} es: {b.obtener_numero_clientes()}")
        case 5:
            try:
                c = int(input(("Escriba el numero de cliente (documento): ")))
                usuario = b.obtenerClienteIndividual(c)
                usuario.crearCuenta()
            except AttributeError:
                print("Este numero de documento no existe en el banco.")
        case 6:
            usuario.meterPlata(b)
        case 7:
            print(b.getAhorros())        
        case 8:
            print(b.getCorrientes())
        case 9:
            print(usuario.getSaldoAhorros())
        case 10:
            print(usuario.getSaldoCorriente())
            
            