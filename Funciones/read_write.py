import json

def read_archiv_json(nombre_archivo):
    with open(nombre_archivo, "r", encoding='utf-8') as file:
        data_readed = json.load(file)
    return data_readed

def write_archiv_json(datos, nombre_archivo):
    #UTF-8 es una codificación de caracteres que puede representar cualquier carácter en el conjunto Unicode, lo que incluye la mayoría de los caracteres utilizados en los idiomas del mundo.
    with open(nombre_archivo, 'w', encoding='utf-8') as file: 
        json.dump(datos, file, indent=4)
