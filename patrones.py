import datetime

def detectar_fuerza_bruta(hallazgos: list[dict]) -> bool:

    timestamps_fallidos = []

    for hallazgo in hallazgos:

        fecha_evento = datetime.datetime.strptime(
            hallazgo["timestamp"],
            "%Y-%m-%d %H:%M:%S"
            )
       
        
        if hallazgo["mensaje"] == "Failed login attempt":
            timestamps_fallidos.append(fecha_evento)


    for i in range(len(timestamps_fallidos) - 2):
        primera_fecha = timestamps_fallidos[i]
        tercera_fecha = timestamps_fallidos[i + 2]

        diferencia = tercera_fecha - primera_fecha

        if diferencia <= datetime.timedelta(seconds=30):
            return True


    return False


