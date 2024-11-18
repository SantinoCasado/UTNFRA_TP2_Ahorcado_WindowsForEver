from Funciones import *

archivo_puntajes =  "scores.json"

def game():
    while True:
        opcion = get_int("BIENVENIDO AL JUEGO DEL AHORCADO\n---- Menú de opciones ----\n1. Jugar. \n2. Puntaje. \n3. Salir.\nIngrese la opcion deseada: ","Error, opcion inexistente",1,3,50)


        match opcion:
            case 1:
                print("-" * 40)

                seleccion_idioma = input("Ingrese el lenguage que quiera [ES | EN]: ").upper()
                while seleccion_idioma != "ES" and seleccion_idioma != "EN":
                    print("OPCION INVALIDA!!!")
                    seleccion_idioma = input("Ingrese el luegage que quiera [ES | EN]: ").upper()

                jugar(seleccion_idioma)
                print("-" * 40)
                pass
            case 2:
                print("*" * 40)
                mostrar_mejores_puntajes(archivo_puntajes)
                print("*" * 40)
            case 3:

                print ("Saliendo del juego.....")
                break

game()