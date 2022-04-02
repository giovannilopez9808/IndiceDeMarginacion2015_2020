from os import makedirs as mkdir


def get_params() -> dict:
    """
    Definicion de las rutas y nombres de los archivos de datos
    """
    params = {
        # Direccion de los archivos de datos
        "path data": "../Data",
        # Nombre de los daros de 1990 a 2015
        "file data 1990": "IMM_1990.csv",
        # Nombre de los datos de 2020
        "file data 2020": "IMM_2020.csv",
        # Nombre del archivo de diccionario de siglas
        "file dictionary": "diccionario.csv",
        # Direccion de los archivos de resultados
        "path results": "../Results",
        # Direccion de las graficas
        "path graphics": "../Graphics",
    }
    # Verificación de la carpeta de resultados
    mkdir(params["path results"],
          exist_ok=True)
    # Verificación de la carpeta de las graficas
    mkdir(params["path graphics"],
          exist_ok=True)
    return params
