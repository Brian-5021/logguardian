
def detectar_evento(evento: dict) -> bool:
    niveles_relevantes = {"WARNING", "ERROR"}

    resultado = evento["tipo"] in niveles_relevantes

    return resultado
        