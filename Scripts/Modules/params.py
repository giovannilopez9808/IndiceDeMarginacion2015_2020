from Modules.cluster_model import cluster_class
from Modules.kmeans import kmeans_model
from Modules.som import SOM_model
from os import makedirs


def get_params() -> dict:
    """
    Definicion de las rutas y nombres de los archivos de datos
    """
    params = {
        # Direccion de los archivos de datos
        "path data": "../Data",
        # Direccion con la informacion del mapa de México
        "path map": "../Data/map",
        # Nombre de los daros de 1990 a 2015
        "file data 1990": "IMM_1990.csv",
        # Nombre de los datos de 2020
        "file data 2020": "IMM_2020.csv",
        "file dictionary": "diccionario.csv",
        # Direccion de los archivos de resultados
        "path results": "../Results",
        # Direccion de las graficas
        "path graphics": "../Graphics",
        "useless columns": [
            "NOM_ENT",
            "NOM_MUN"
        ],
        "embedding columns": [
            'POB_TOT',
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
                         "color": "#03045e",
                         },
            'Bajo': {"id": 1,
                     "color": "#0077b6",
                     },
            'Medio': {"id": 2,
                      "color": "#00b4d8",
                      },
            'Alto': {"id": 3,
                     "color": "#90e0ef",
                     },
            'Muy alto': {"id": 4,
                         "color": "#caf0f8",
                         },
        },
        "SOM colors": {
            0: "#ef476f",
            1: "#ffd166",
            2: "#06d6a0",
            3: "#118ab2",
            4: "#f3722c",
        },
        # Parametros para el método de PCA
        "PCA": {
            "kernels": {
                "linear": {"elevation": 19},
                "rbf": {"elevation": 0},
                "cosine": {"elevation": 0},
                "sigmoid": {"elevation": 0}
            },
            "2D": {"components": 2},
            "3D": {"components": 3},
        },
        "isomap": {
            "neighbors": {8: {"elevation": 34},
                          10: {"elevation": 34},
                          12: {"elevation": 34},
                          14: {"elevation": 34}},
            "2D": {"components": 2},
            "3D": {"components": 3}
        },
        "TSNE": {
            "perplexity": {
                100: {"elevation": 0},
                200: {"elevation": 0},
                300: {"elevation": 0},
                400: {"elevation": 0}
            },
            "2D": {"components": 2},
            "3D": {"components": 3}
        },
        "LLE": {
            "2D": {"components": 2,
                   "neighbors": [4, 5, 6, 7]},
            "3D": {"components": 3,
                   "neighbors": [2, 3, 4, 6]}
        },
        "Kmeans": {
            "k-means++",
            "random",
        }
    }
    # Verificación de la carpeta de resultados
    mkdir(params["path results"])
    # Verificación de la carpeta de las graficas
    mkdir(params["path graphics"])
    return params


def get_metrics_params() -> dict:
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
                "filename": "Kmeans.csv",
                "file graphics": "Kmeans++_confusion_matrix.png",
                "class": kmeans_model,
                "label": "k-means++"
            },
            "Kmeans": {
                "filename": "Kmeans.csv",
                "file graphics": "Kmeans_random_confusion_matrix.png",
                "class": kmeans_model,
                "label": "random"
            },
        }
    }
    return datasets


def mkdir(path) -> None:
    makedirs(path,
             exist_ok=True)


def get_classes_colors(params: dict) -> dict:
    colors = {}
    for classes in params["classes"]:
        data = params["classes"][classes]
        color = data["color"]
        colors[classes] = color
    return colors
