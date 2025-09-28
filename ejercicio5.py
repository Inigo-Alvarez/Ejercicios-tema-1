import random

def generar_adn(n):
    bases = ["A", "T", "C", "G"]
    
    # Generar cadena aleatoria
    cadena = "".join(random.choice(bases) for _ in range(n))
    
    # Contar ocurrencias de cada base
    conteo = {base: cadena.count(base) for base in bases}
    
    print("Cadena de ADN generada:", cadena)
    print("Conteo de bases:", conteo)
    
    return cadena, conteo


# Ejemplo de uso
cadena, conteo = generar_adn(20)
