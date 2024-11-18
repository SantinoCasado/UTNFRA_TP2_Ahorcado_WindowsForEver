def validate_number(dato: int) -> bool:
    try:
        int(dato)
        return True
    except ValueError:
        return  False

def validate_lenght(str,lenght):
    try:
        if len(str) <= lenght:
            return str
        
    except ValueError:
        return None

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> (int | None):
    dato_ingresado = input(mensaje)
    
    # Primero validamos el tipo de dato.
    if validate_number(dato_ingresado):
        dato_convertido = int(dato_ingresado)
        
        # Luego validamos que se encuentre dentro del rango.
        if dato_convertido >= minimo and dato_convertido <= maximo:
            return dato_convertido
        else:
            print(mensaje_error)
            if reintentos > 0:
                return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
            else:
                return None
    else:
        print(mensaje_error)
        if reintentos > 0:
            return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
        else:
            return None

def get_str(mensaje:str,mensaje_error:str, longitud:int) -> str|None: 
    user_input = str(input(mensaje))
    string = validate_lenght(user_input,longitud)
    if string is not None:
        return string
    else: 
        print(mensaje_error)
    
    return None

def validar_entero(numero):
    while True:
        try:
            valor = int(input(numero))
            return valor
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def validar_lista_existente(lista):
    if lista == []:
        return True
    else:
        return False
    
def validar_letra (letra, palabra):
    for i in range (len(palabra)):
        if letra == palabra[i]:
            return True
    return False