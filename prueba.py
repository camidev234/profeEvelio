from os import strerror

try:
    listaArchivos = []
    while True:
        print("1.Crear archivo")
        print("3.Abrir archivo")
        print("3.Salir")
        opc = int(input("Escoja que desea hacer: "))
        match opc:
            case 1:
                nombreArchivo = input("Escriba el nombre del archivo que quiere crear: ")
                estado = True
                while nombreArchivo in listaArchivos:
                    print("El archivo ya existe si quiere abrir si desea cancelar digite 9")
                    nombreArchivo = input("Escriba el nombre del archivo que quiere crear: ")
                    if nombreArchivo == "9":
                        estado = False
                        break
                if estado:
                    print(f"Archivo {nombreArchivo} creado con exito")
                    stream = open(nombreArchivo, "wt")
                    stream.close()
                    listaArchivos.append(nombreArchivo)
            case 2:
                nombreArchivo = input("Escriba el nombre del archivo que quiere abrir:" )
                status = True
                while nombreArchivo not in listaArchivos:
                    print("Archivo no existente, si desea cancelar escriba 9")
                    nombreArchivo = input("Escriba el nombre del archivo: ")
                    if nombreArchivo == "9":
                        status = False
                        break
                if status:
                    for n in listaArchivos:
                        if n == nombreArchivo:
                            archivo = n
                    while True:
                        print("""
                    1. Lectura
                    2. Escritura  
                        """)  
                        mode = int(input("Escoja en que modo desea abrir su archivo: "))
                        match mode:
                            case 1:
                                file = open(nombreArchivo, "rt")
                                for k in file.read():
                                    print(k, end="") 
                                file.close()
                            case 2:
                                file = open(nombreArchivo, "a")
                                a = input("Escriba lo que que quiere agregar presione enter:  ")
                                cadena = a + "\n"
                                file.write(cadena)
                                file.close()
                                
            case 3:
                break           
except IOError as e:
	print("Se produjo un error de E/S:", strerror(e.errno))