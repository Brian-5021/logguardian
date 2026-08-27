
def analizar_linea(linea: str, numero_linea: int) -> dict | None:

    niveles = {"ERROR", "WARNING", "INFO"}
    partes = linea.split(" ", 1)
    tipo = partes[0]

    if tipo in niveles:
        resultado = {
        "linea": numero_linea,
        "tipo" : partes[0],
        "mensaje" : partes[1]
        }
    else:
        resultado = None

    return resultado

    
print(analizar_linea("ERROR Database connection failed", 3))
print(analizar_linea("WARNING Failed login attempt", 4))
print(analizar_linea("INFO User logged in", 8))
print(analizar_linea("User logged in", 112))