def analizar_linea(linea: str, numero_linea: int) -> dict | None:

    niveles = {"ERROR", "WARNING", "INFO"}
    partes = linea.split(" ", 4)
    tipo = partes[2]

    if tipo in niveles:
        resultado = {
            "linea": numero_linea,
            "timestamp": partes[0] + " " + partes[1],
            "tipo": partes[2],
            "ip": partes[3],
            "mensaje": partes[4]
        }
    else:
        resultado = None

    return resultado

