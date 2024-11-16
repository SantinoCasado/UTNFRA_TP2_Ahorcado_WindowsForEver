from Funciones import *


flag =  True
def ahorcados():
    while flag:
        opcion = get_int("BIENVENIDO AL JUEGO DEL AHORCADO\n---- Menú de opciones ----\n1. Jugar. \n2. Puntaje. \n3. Salir.\nIngrese la opcion deseada: ","Error, opcion inexistente",1,3,50)

        match opcion:
            case 1:
                print("-" * 40)
                language = str(input("Seleccione un idioma[ES | EN]: ")).upper()
                while language != "ES" and language != "EN":
                    print("Opcion incorrecta!!")
                    language = str(input("Seleccione un idioma[ES | EN]: ")).upper()
                nombre = str(input("Ingrese su nombre: "))

                jugar(language, nombre)

                pass
                print()
            case 2:
                pass
                print()
            case 3:
                print ("Saliendo del juego.....")
                flag = False

ahorcados()