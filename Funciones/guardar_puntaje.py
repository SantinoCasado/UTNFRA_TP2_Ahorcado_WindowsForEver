import json

def guardar_puntaje(nombre_archivo, nombre_jugador, puntaje):
    try:
        with open(nombre_archivo, 'r') as file:
            content = file.read().strip()
            if content:
                puntajes = json.loads(content)
            else:
                puntajes = []
    except FileNotFoundError:
        puntajes = []
    
    # Buscamos si el jugador ya existe en la lista de puntajes
    jugador_existente = False
    for jugador in puntajes:
        if jugador["nombre"] == nombre_jugador:
            jugador["puntaje"] += puntaje  # Actualizamos el puntaje sumando el nuevo
            jugador_existente = True
            break
    
    # Si el jugador no existe, lo añadimos a la lista
    if not jugador_existente:
        puntajes.append({"nombre": nombre_jugador, "puntaje": puntaje})
    
    # Guardamos la lista de puntajes actualizada en el archivo JSON
    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        json.dump(puntajes, file, ensure_ascii=False, indent=4)

