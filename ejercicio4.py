def calculadora_notas(notas):
    media = sum(notas) / len(notas)
    nota_max = max(notas)
    nota_min = min(notas)
    
    print("Notas:", notas)
    print("Media:", media)
    print("Nota más alta:", nota_max)
    print("Nota más baja:", nota_min)
    
    if any(nota < 5 for nota in notas):
        print("Hay al menos una nota suspensa.")
    
    return media, nota_max, nota_min


# Ejemplo de uso
lista_notas = [7, 4, 9, 10, 5, 3]
calculadora_notas(lista_notas)
