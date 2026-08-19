from pathlib import Path

def buscar_archivos(ruta: str) -> list[str]:

    ruta = Path(ruta)

    if not ruta.exists():

        raise FileNotFoundError("La ruta indicada no existe.")
    
    if not ruta.is_dir():

        raise NotADirectoryError("La ruta indicada no es una carpeta.")

    rutas = ruta.glob("*.log")

    resultado = [str(archivo) for archivo in rutas]

    return resultado



def leer_log(ruta: str) -> list[str]:
    lineas = []

    with open(ruta, "r") as archivo:

        for linea in archivo:
            lineas.append(linea.rstrip())
            
        return lineas
