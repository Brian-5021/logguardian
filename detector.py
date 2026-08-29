
def detectar_evento(evento: dict) -> bool:
    niveles_relevantes = {"WARNING", "ERROR"}

    resultado = evento["tipo"] in niveles_relevantes

    return resultado


print(detectar_evento({
    "linea": 2,
    "tipo": "WARNING",
    "mensaje": "Failed login attempt"
}))

print(detectar_evento({
    "linea": 3,
    "tipo": "ERROR",
    "mensaje": "Database connection failed"
}))

print(detectar_evento({
    "linea": 1,
    "tipo": "INFO",
    "mensaje": "User logged in"
}))
        