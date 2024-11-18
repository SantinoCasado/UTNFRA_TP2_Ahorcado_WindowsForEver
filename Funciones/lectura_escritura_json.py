import json

# Creamos una funcion que SOLO lea y retorne los valores de un archivo json cualquiera
def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, "r", encoding='utf-8') as file:
        datos_leidos = json.load(file)
    return datos_leidos

# Sobre un archivo json cualquiera escribimos unos datos en especifico
def escribir_archivo_json(datos, nombre_archivo):
    # Debido a que los datos incluyen palabras en ingles utiliza UTF-8 que es una codificación de caracteres que puede representar cualquier carácter en el conjunto Unicode, lo que incluye la mayoría de los caracteres utilizados en los idiomas del mundo.
    with open(nombre_archivo, 'w', encoding='utf-8') as file: 
        json.dump(datos, file, indent=4)