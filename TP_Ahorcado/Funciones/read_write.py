import json

def read_archiv_json(nombre_archivo):
    with open(nombre_archivo, "r") as file:
        data_readed = json.load(file)
    return data_readed

def write_archiv_json(datos, nombre_archivo):
    with open(nombre_archivo, 'w') as file: 
        json.dump(datos, file, indent=4)
