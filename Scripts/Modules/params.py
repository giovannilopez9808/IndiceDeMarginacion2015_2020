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
        "useless columns": ["NOM_ENT",
                            "NOM_MUN"],
        "embedding columns": [
            'ANALF',
            'SBASC',
            'OVSDE',
            'OVSEE',
            'OVSAE',
            'OVPT',
            'VHAC',
            'PL.5000',
            'PO2SM'
        ],
        "classes": {
            'Muy bajo': {"id": 0,
                         "color": "#ef476f"},
            'Bajo': {"id": 1,
                     "color": "#ffd166"},
            'Medio': {"id": 2,
                      "color": "#06d6a0"},
            'Alto': {"id": 3,
                     "color": "#118ab2"},
            'Muy alto': {"id": 4,
                         "color": "#f3722c"},
        }
    }
    # Verificación de la carpeta de resultados
    mkdir(params["path results"],
          exist_ok=True)
    # Verificación de la carpeta de las graficas
    mkdir(params["path graphics"],
          exist_ok=True)
    return params
