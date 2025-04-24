import random
import json
from .lectura_escritura_json import escribir_archivo_json, leer_archivo_json

# Nombre del archivo JSON
nombre_archivo_data = "data.json"

# Diccionario con las palabras
datos = {
    "ahorcado": [
        {"id": 1, "ES": "elefante", "EN": "elephant"},
        {"id": 2, "ES": "departamento", "EN": "department"},
        {"id": 3, "ES": "medicina", "EN": "medicine"},
        {"id": 4, "ES": "ingenieria", "EN": "engineering"},
        {"id": 5, "ES": "computadora", "EN": "computer"},
        {"id": 6, "ES": "dispositivo", "EN": "device"},
        {"id": 7, "ES": "software", "EN": "software"},
        {"id": 8, "ES": "hardware", "EN": "hardware"},
        {"id": 9, "ES": "idioma", "EN": "language"},
        {"id": 10, "ES": "ciudadano", "EN": "citizen"}
    ]
}

# Escribir el JSON una sola vez al inicio (no en cada llamada a la función)
try:
    escribir_archivo_json(datos, nombre_archivo_data)
except Exception as e:
    print(f"Error al escribir el archivo JSON: {e}")

# Función para elegir palabra aleatoria en el idioma indicado
def eleccion_aleatoria(idioma):
    try:
        informacion = leer_archivo_json(nombre_archivo_data)
    except (FileNotFoundError, json.JSONDecodeError):
        return "Error: archivo JSON no encontrado o con formato inválido."
    
    eleccion = random.choice(informacion["ahorcado"])
    
    # Validamos que el idioma esté presente en la estructura del diccionario
    if idioma in eleccion:
        return eleccion[idioma]
    else:
        return "Idioma no válido"
