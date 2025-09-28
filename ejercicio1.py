def decodificar_mensaje(mensaje):
    # Voltear la cadena usando slicing
    invertido = mensaje[::-1]
    
    # Filtrar solo las letras con isalpha()
    limpio = ""
    for caracter in invertido:
        if caracter.isalpha():
            limpio += caracter
    
    return limpio

# Mensaje de prueba
mensaje_secreto = "**odnumM,aloH*"
resultado = decodificar_mensaje(mensaje_secreto)

print("Mensaje original:", mensaje_secreto)
print("Mensaje decodificado:", resultado)
