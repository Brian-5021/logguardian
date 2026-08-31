
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
