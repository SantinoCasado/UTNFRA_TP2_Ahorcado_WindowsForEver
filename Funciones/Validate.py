def validate_number(number, min, max) :
    try:
        if min <= number <= max:
            return number
        
    except ValueError:
        return None

def validate_lenght(str,lenght):
    try:
        if len(str) <= lenght:
            return str
        
    except ValueError:
        return None

def get_int(mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos:int):
    
    for _ in range(reintentos):
        user_input = int(input(mensaje))
        numero = validate_number(user_input,minimo,maximo)
        if numero is not None:
            return numero
        else: 
            print(mensaje_error)
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