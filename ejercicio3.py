def clasificar_numeros(lista):
    pares = []
    impares = []
    negativos = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
        
        if numero < 0:
            negativos.append(numero)
    
    return pares, impares, negativos


# Ejemplo de uso
numeros = [10, -3, 7, -8, 0, 15, -22, 4]
pares, impares, negativos = clasificar_numeros(numeros)

print("Lista original:", numeros)
print("Números pares:", pares)
print("Números impares:", impares)
print("Números negativos:", negativos)
