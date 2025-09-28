def inventario_personajes(personajes):
    # Filtrar humanos y criaturas
    humanos = [nombre for nombre, tipo in personajes.items() if tipo == "humano"]
    criaturas = [nombre for nombre, tipo in personajes.items() if tipo == "criatura"]
    
    # Ordenar humanos alfabéticamente
    humanos_ordenados = sorted(humanos)
    
    # Ordenar criaturas por longitud de nombre
    criaturas_ordenadas = sorted(criaturas, key=len)
    
    return humanos_ordenados, criaturas_ordenadas


# Ejemplo de uso con otros nombres
personajes = {
    "Carlos": "humano",
    "Elena": "humano",
    "Martín": "humano",
    "Dragón": "criatura",
    "Kraken": "criatura",
    "Hidra": "criatura"
}

humanos, criaturas = inventario_personajes(personajes)

print("Humanos ordenados alfabéticamente:", humanos)
print("Criaturas ordenadas por longitud de nombre:", criaturas)
