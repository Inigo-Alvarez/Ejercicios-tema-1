def analizar_url(url):
    try:
        # Separar protocolo
        if "://" not in url:
            raise ValueError("La URL no contiene un protocolo válido (http o https).")
        
        protocolo, resto = url.split("://", 1)
        
        # Separar dominio y recurso
        if "/" in resto:
            dominio, recurso = resto.split("/", 1)
        else:
            dominio, recurso = resto, None
        
        return protocolo, dominio, recurso
    
    except Exception as e:
        return f"Error al analizar la URL: {e}"


# Ejemplos de uso
print(analizar_url("https://www.ejemplo.com/index.html"))
print(analizar_url("http://misitio.org"))
print(analizar_url("ftp://archivo.net/documento.pdf"))
