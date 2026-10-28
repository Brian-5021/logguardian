def mostrar_reporte(resultados: dict) -> None:

    for archivo, datos in resultados.items():
        print(f"Archivo: {archivo}")

        fuerza_bruta = datos["patrones"]["fuerza_bruta"]
        ip_detectada = datos["patrones"]["ip"]
        total_intentos = datos["patrones"]["total_eventos"]

        duracion_segundos = datos["patrones"]["duracion_segundos"]
        eventos_en_secuencia = len(datos["patrones"]["eventos_detectados"])

        if fuerza_bruta:
            print("Fuerza bruta: DETECTADA")
            print(f"Total de intentos fallidos encontrados: {total_intentos}")
            print(f"IP detectada: {ip_detectada}")
            print(f"Duración: {duracion_segundos} segundos")
            print(f"Eventos en secuencia: {eventos_en_secuencia}")
        else:
            print("Fuerza bruta: NO DETECTADA")

        print("-" * 40)

        