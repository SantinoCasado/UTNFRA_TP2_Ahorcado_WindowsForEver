from read_write import *
from elegir_palabra import *
from etapas_monigote import *
from guardar_puntaje import *
from Validate import validar_letra


def posicion_letra (letra, palabra):
    posiciones = []
    for i in range (len(palabra)):
        if letra == palabra[i]:
            posiciones.append(i)
    return posiciones

def jugar(idioma, nombre_jugador):
    #Asignamos variables necesarias 
    intentos_max = 6 
    intento_actual = 0 
    palabra = eleccion_aleatoria(idioma) 
    palabra_oculta = "_" * len(palabra) 
    letras_usadas = []
    letras_acertadas = []
    puntaje = 0
    
    #Inciamos el juego
    while intento_actual < intentos_max: 
        dibujar_monigote(intento_actual)
        print("Intentos restantes: ", intentos_max - intento_actual)
        print("Letras usadas: ", letras_usadas)
        print(palabra_oculta)
        letra = str(input("Ingrese una letra: ")).lower()
        while len(letra) > 0 or letra == "" or not letra.isalpha():
            print("Seleccione UNA LETRA")
            letra = str(input("Ingrese una letra: ")).lower()
        
        #Validamos que ya haya usado la letra
        if letra in letras_usadas: 
            print("YA HAS USADO ESA LETRA. INTENTA CON OTRA") 
            continue 
        else:
            # Sino la agregamos
            letras_usadas.append(letra)

        #Validamos y remplazamos si le atino a la letra
        if validar_letra(letra, palabra): 
            print("¡Bien hecho! Adivinaste una letra.")
            puntaje += 1

            posiciones_encontradas = posicion_letra(letra, palabra) #Nos devuelve una lista con los indices
            palabra_oculta = list(palabra_oculta)   #Convertimos la palabra oculta a un lista para poder modificar por idice

            for posicion in posiciones_encontradas: #Por cada indice en la lista de indices encontrados
                palabra_oculta[posicion] = letra    #Reemplazamos por la letra
            palabra_oculta = "".join(palabra_oculta)    #Volvemos a unirlo todo en una str

        #Si no le pega
        else:
            intento_actual += 1
            print("Letra incorrecta")
        
        #Validamos si adivino la palabra
        if "_" not in palabra_oculta: 
            print("¡Felicidades! Has adivinado la palabra:", palabra) 
            print("Puntaje guardado.")
            flag = False
        

    print("\nHas perdido. La palabra era:", palabra) 
    dibujar_monigote(intento_actual)

    guardar_puntaje("scores.json", nombre_jugador, puntaje) 
    print("Puntaje guardado.")


jugar("ES", "santino")