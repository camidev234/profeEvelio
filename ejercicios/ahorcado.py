import random

listaPalabras = []

print("""
1. Agregar Palabras
2. Jugar
3. Salir
      
""")

while True:
    try:
        pregunta = int(input("Escoja una opcion: "))
    except ValueError:
        print("Valor no valido.")
        
    match pregunta:
        case 1:
            palabra = input("Escriba la palabra que desea agregar: ")
            listaPalabras.append(palabra)
        case 2:
            intentos = 10
            coincidencias = 0
            palabraFinal = []
            palabra = []
            guia = []
            palabraEnUso = []
            palabraElegida = random.choice(listaPalabras)
            
            for i in palabraElegida:
                palabraEnUso.append(i)
                guia.append("_")
                
            print(guia)
            contVueltas = 0
            while True:
                contVueltas+=1
                
                letra = input("Escriba la letra: ")
                
                if letra in palabraFinal:
                    print("La letra ya esta en la palabra.")
                
                if contVueltas==1:
                    for i in palabraEnUso:
                        if letra == i:
                            coincidencias+=1
                            palabraFinal.append(i)
                        else:
                            palabraFinal.append("_")
                    if coincidencias == 0:
                        intentos-=1
                        print(f"Letra incorrecta le quedan {intentos} intentos.") 
                    else:
                        coincidencias = 0
                               
                    print(palabraFinal)
                else:
                    for l in range(len(palabraEnUso)):
                        if letra == palabraEnUso[l]:
                            coincidencias+=1
                            palabraFinal[l] = letra
                            
                    if coincidencias == 0:
                        intentos-=1
                        print(f"Letra incorrecta le quedan {intentos} intentos.") 
                    else:
                        coincidencias = 0
                        
                    print(palabraFinal)
                        
                if palabraFinal == palabraEnUso:
                    print("Muy bien adivinaste La palabra.")
                    break     
                    
                if intentos == 0:
                    print(f"¡Ahorcado!, No adivinaste la palabra, la palabra era: {palabraEnUso}")
                    break