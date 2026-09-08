
def analizar_linea(linea: str, numero_linea: int) -> dict | None:

    niveles = {"ERROR", "WARNING", "INFO"}
    partes = linea.split(" ", 3)
    tipo = partes[2]

    if tipo in niveles:
        resultado = {
        "linea": numero_linea,
        "timestamp": partes[0] + " " + partes[1],
        "tipo" : partes[2],
        "mensaje": partes[3]
        }
    else:
        resultado = None

    return resultado

