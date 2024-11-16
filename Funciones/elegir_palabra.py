import random
from read_write import *
import json

nombre_archivo_data = "data.json"
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
    carga = write_archiv_json(datos, nombre_archivo_data)
    informacion = read_archiv_json(nombre_archivo_data)

    eleccion_aleatoria = random.choice(informacion["ahorcado"])
    return eleccion_aleatoria[idiomna]
