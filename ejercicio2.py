def simulador_ahorro(cantidad_inicial, cantidad_mensual, meses):
    # Calcular el total ahorrado
    total = cantidad_inicial + (cantidad_mensual * meses)
    
    # Mostrar resultado
    print(f"Total ahorrado al final de {meses} meses: {total} €")
    
    # Comprobar condición extra
    if total > 5000:
        print("¡Felicidades! Has superado los 5000 € de ahorro.")
    
    return total


# Ejemplo de uso
cantidad_inicial = 2000
cantidad_mensual = 300
meses = 12

simulador_ahorro(cantidad_inicial, cantidad_mensual, meses)
