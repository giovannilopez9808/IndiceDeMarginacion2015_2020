from Modules.cluster_model import cluster_class
from Modules.kmeans import kmeans_model
from Modules.som import SOM_model
from os.path import join
from os import makedirs


def get_params(year: int) -> dict:
    """
    Definicion de las rutas y nombres de los archivos de datos
    """
    params = {
        # Direccion de los archivos de datos
        "path data":
        "../Data",
        # Direccion con la informacion del mapa de México
        "path map":
        "../Data/map",
        # Nombre de los daros de 1990 a 2015
        "file data 2015":
        "IMM_1990.csv",
        # Nombre de los datos de 2020
        "file data 2020":
        "IMM_2020.csv",
        "file dictionary":
        "diccionario.csv",
        # Direccion de los archivos de resultados
        "path results":
        "../Results",
        # Direccion de las graficas
        "path graphics":
        "../Graphics",
        # Columnas de datos que nunca seran usadas
        "useless columns": ["NOM_ENT", "NOM_MUN"],
        # Columnas de datos usadas para crear el embedding
        "embedding columns": [
            'ANALF', 'SBASC', 'OVSDE', 'OVSEE', 'OVSAE', 'OVPT', 'VHAC',
            'PL.5000', 'PO2SM'
        ],
        # Clase de tipo de marginación, se le da un id y un color
        "classes": {
            'Muy bajo': {
                "id": 0,
                "color": "#b7094c",
            },
            'Bajo': {
                "id": 1,
                "color": "#892b64",
            },
            'Medio': {
                "id": 2,
                "color": "#5c4d7d",
            },
            'Alto': {
                "id": 3,
                "color": "#2e6f95",
            },
            'Muy alto': {
                "id": 4,
                "color": "#0091ad",
            },
        },
        # Parametros para el método de PCA
        "PCA": {
            "kernels": {
                "linear": {
                    "elevation": 19,
                    "Name": "linela"
                },
                "rbf": {
                    "elevation": 0,
                    "Name": "Gaussiano"
                },
                "cosine": {
                    "elevation": 0,
                    "Name": "Coseno"
                },
                "sigmoid": {
                    "elevation": 0,
                    "Name": "Sigmoide"
                }
            },
            "2D": {
                "components": 2,
                "file results": "PCA_2D.csv",
                "file graphics": "PCA_2D.png"
            },
            "3D": {
                "components": 3,
                "file animation format": "PCA_3D_{}",
                "file results": "PCA_3D.csv"
            },
        },
        # Parametros para el método ISOMAP
        "ISOMAP": {
            "neighbors": {
                8: {
                    "elevation": 34
                },
                10: {
                    "elevation": 34
                },
                12: {
                    "elevation": 34
                },
                14: {
                    "elevation": 34
                }
            },
            "2D": {
                "components": 2,
                "file graphics": "ISOMAP_2D.png",
                "file results": "ISOMAP_2D.csv"
            },
            "3D": {
                "components": 3,
                "file animation format": "ISOMAP_3D_{}",
                "file results": "ISOMAP_3D.csv"
            },
        },
        # Parametros para el método de TSNE
        "TSNE": {
            "perplexity": {
                100: {
                    "elevation": 0
                },
                200: {
                    "elevation": 0
                },
                300: {
                    "elevation": 0
                },
                400: {
                    "elevation": 0
                }
            },
            "2D": {
                "components": 2,
                "file results": "TSNE_2D.csv",
                "file graphics": "TSNE_2D.png"
            },
            "3D": {
                "components": 3,
                "file animation format": "TSNE_3D_{}",
                "file results": "TSNE_3D.csv"
            },
        },
        # Parametros para el método de LLE (no se uso)
        "LLE": {
            "neighbors": [4, 5, 6, 7],
            "2D": {
                "components": 2,
                "filenane": "LLE_2D.csv"
            },
            "3D": {
                "components": 3,
                "filenane": "LLE_3D.csv"
            },
        },
        # Parametros para el método de Kmeans
        "Kmeans": {
            "k-means++",
            "random",
        }
    }
    # Colores usados para el metodo SOM
    params["SOM colors"] = _define_SOM_colors(params)
    # Elección del archivo de datos de CONAPO que se analizara
    params["file CONAPO data"] = _define_CONAPO_data(params, year)
    # Define la direccion de resultados y graficas dado el archivo a analizar
    params = _define_year_folders(params, year)
    # Verificación de la carpeta de resultados
    mkdir(params["path results"])
    # Verificación de la carpeta de las graficas
    mkdir(params["path graphics"])
    return params


def get_metrics_params() -> dict:
    """
    Dataset para obtener de forma automatica las metricas de cada modelo usado
    """
    datasets = {
        "Models": {
            "SOM": {
                "filename": "SOM.csv",
                "file graphics": "SOM_confusion_matrix.png",
                "class": SOM_model,
                "label": "SOM labels",
            },
            "Cluster": {
                "filename": "Cluster.csv",
                "file graphics": "Cluster_confusion_matrix.png",
                "class": cluster_class,
                "label": "Cluster labels",
            },
            "Kmeans++": {
                "filename": "kmeans_k-means++.csv",
                "file graphics": "Kmeans++_confusion_matrix.png",
                "class": kmeans_model,
                "label": "k-means++"
            },
            "Kmeans": {
                "filename": "kmeans_random.csv",
                "file graphics": "Kmeans_random_confusion_matrix.png",
                "class": kmeans_model,
                "label": "random"
            },
        }
    }
    return datasets


def mkdir(path) -> None:
    """
    Estandarización para la creacion de carpetas
    """
    makedirs(path, exist_ok=True)


def get_classes_colors(params: dict) -> dict:
    """
    Obtiene un diccionario de colores para cada tipo de dato
    """
    colors = {}
    for classes in params["classes"]:
        data = params["classes"][classes]
        color = data["color"]
        colors[classes] = color
    return colors


def _define_year_folders(params: dict, year: int) -> dict:
    """
    Definición de las carpetas de resultados y graficas para cada tipo de archivo a analizar
    """
    folder = "Data_{}".format(year)

    params["path graphics"] = join(params["path graphics"], folder)
    params["path results"] = join(params["path results"], folder)
    return params


def _define_CONAPO_data(params: dict, year: int) -> str:
    """
    Define el archivo que se usara para realizar el analisis
    """
    label = "file data {}".format(year)
    return params[label]


def _define_SOM_colors(params: dict) -> dict:
    """
    Colores usados para el metodo SOM
    """
    colors = {}
    for classes in params["classes"]:
        dataset = params["classes"][classes]
        id = dataset["id"]
        color = dataset["color"]
        colors[id] = color
    return colors


def define_filenames_2D(params: dict, model: str) -> dict:
    """
    Define el nombre de los archivos dado un modelo para el caso bidimensional
    """
    params["file graphics"] = params[model]["2D"]["file graphics"]
    params = define_file_results(params, model, "2D")
    return params


def define_filenames_3D(params: dict, model: str) -> dict:
    """
    Define el nombre de los archivos dado un modelo para el caso tridimensioanl
    """
    params = define_file_results(params, model, "3D")
    return params


def define_file_results(params: dict, model: str, dim: str) -> dict:
    """
    Define el nombre de los archivos dado un modelo y su dimension
    """
    params["file results"] = params[model][dim]["file results"]
    return params


def define_file_animation(dataset: dict, param: str) -> str:
    """
    Define el nombre de la animacion
    """
    filename = dataset["3D"]["file animation format"].format(param)
    return filename
