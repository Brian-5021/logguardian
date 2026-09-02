from lector import buscar_archivos, leer_log
from analizador import analizar_linea
from detector import detectar_evento
from patrones import detectar_fuerza_bruta

def procesar_logs(ruta: str) -> dict:
    resultados = {}

    for archivo in buscar_archivos(ruta):
        lineas = leer_log(archivo)
        hallazgos = []
        patrones = {}

        for numero_linea, linea in enumerate(lineas, start=1):
            linea_actual = analizar_linea(linea, numero_linea)

            if linea_actual is not None:
                es_evento = detectar_evento(linea_actual)

                if es_evento:
                    hallazgos.append(linea_actual)

        patrones["fuerza_bruta"] = detectar_fuerza_bruta(hallazgos)
                
        resultados[archivo] = {
            "hallazgos": hallazgos,
            "patrones": patrones
        }


    return resultados


print(procesar_logs("logs"))

