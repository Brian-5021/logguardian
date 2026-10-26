def mostrar_reporte(resultados: dict) -> None:

    for archivo, datos in resultados.items():
        print(f"Archivo: {archivo}")

        fuerza_bruta = datos["patrones"]["fuerza_bruta"]
        ip_detectada = datos["patrones"]["ip"]
        total_intentos = datos["patrones"]["total_eventos"]

        duracion_segundos = datos["patrones"]["duracion_segundos"]


        if fuerza_bruta:
            print("Fuerza bruta: DETECTADA")
            print(f"Total de intentos de fuerza bruta: {total_intentos}")
            print(f"IP detectada: {ip_detectada}")
            print(f"Duración: {duracion_segundos} segundos")
        else:
            print("Fuerza bruta: NO DETECTADA")

        print("-" * 40)

        