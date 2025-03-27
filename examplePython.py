

def invertir(cadena):
    if len(cadena) <= 1:  # Condición base: si la cadena tiene 0 o 1 caracteres, se regresa igual
        return cadena
    else:
        return invertir(cadena[1:]) + cadena[0]  # Llamada recursiva con el resto de la cadena
    
    print(invertir("python"))
