from lector import buscar_archivos, leer_log


def procesar_logs(ruta: str) -> dict:
    resultados = {}

    for archivo in buscar_archivos(ruta):
        resultados[archivo] = leer_log(archivo)


    return resultados

