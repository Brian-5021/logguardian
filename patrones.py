def detectar_fuerza_bruta(hallazgos: list[dict]) -> bool:

    intentos_fallidos = 0

    for hallazgo in hallazgos:
       if hallazgo["mensaje"] == "Failed login attempt":
            intentos_fallidos += 1

    return intentos_fallidos >= 3

    