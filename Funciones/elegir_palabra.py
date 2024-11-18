import random 
from .lectura_escritura_json import * 
import json

# Establecemeos nombre del archivo
nombre_archivo_data = "data.json"
# Utilizando un diccionario generamos los contenidos
datos = {
    "ahorcado": [
        {
            "id": 1,
            "ES": "elefante",
            "EN": "elephant"
        },
        {
            "id": 2,
            "ES": "departamento",
            "EN": "department"
        },
        {
            "id": 3,
            "ES": "medicina",
            "EN": "medicine"
        },
        {
            "id": 4,
            "ES": "ingenieria",
            "EN": "engineering"
        },
        {
            "id": 5,
            "ES": "computadora",
            "EN": "computer"
        },
        {
            "id": 6,
            "ES": "dispositivo",
            "EN": "device"
        },
        {
            "id": 7,
            "ES": "software",
            "EN": "software"
        },
        {
            "id": 8,
            "ES": "hardware",
            "EN": "hardware"
        },
        {
            "id": 9,
            "ES": "idioma",
            "EN": "language"
        },
        {
            "id": 10,
            "ES": "ciudadano",
            "EN": "citizen"
        }
    ]
}

#Punto A/B
def eleccion_aleatoria (idiomna):
    # Cargamos el archivo con los datos
    escribir_archivo_json(datos, nombre_archivo_data)
    # Guardamos en una variabel toda el contenido
    informacion = leer_archivo_json(nombre_archivo_data)

    # Utilizando el random selecciona una palabra DEPENDIENDO del idioma
    eleccion_aleatoria = random.choice(informacion["ahorcado"])
    return eleccion_aleatoria[idiomna]
