import datetime

patrones_login = {
    "failed_login_attempt": "Failed login attempt",
    "failed_login_user": "Failed login for user",
    "authentication_failure": "Authentication failure",
    "invalid_password": "Invalid password",
    "login_failed_user": "Login failed for user"
}

def detectar_fuerza_bruta(hallazgos: list[dict]) -> dict:

    eventos_fallidos = []

    for hallazgo in hallazgos:

        fecha_evento = datetime.datetime.strptime(
            hallazgo["timestamp"],
            "%Y-%m-%d %H:%M:%S"
            )
       
        mensaje_normalizado = hallazgo["mensaje"].lower()
        for nombre, patron in patrones_login.items():
            
            patron_normalizado = patron.lower()
            if patron_normalizado in mensaje_normalizado:
                eventos_fallidos.append({
                    "timestamp": fecha_evento,
                    "patron": nombre,
                    "ip": hallazgo["ip"],
                    "mensaje": hallazgo["mensaje"]
                })
                break

    fuerza_bruta = False
    primer_evento = None
    ultimo_evento = None
    duracion_segundos = 0

    for i in range(len(eventos_fallidos) - 2):
        primera_fecha = eventos_fallidos[i]["timestamp"]
        tercera_fecha = eventos_fallidos[i + 2]["timestamp"]

        diferencia = tercera_fecha - primera_fecha

        if diferencia <= datetime.timedelta(seconds=30):
            fuerza_bruta = True
            primer_evento = primera_fecha
            ultimo_evento = tercera_fecha
            duracion_segundos = diferencia.total_seconds()
            break

    return {
    "fuerza_bruta": fuerza_bruta,
    "eventos": eventos_fallidos,
    "total_eventos": len(eventos_fallidos),
    "primer_evento": primer_evento,
    "ultimo_evento": ultimo_evento,
    "duracion_segundos": duracion_segundos
}


