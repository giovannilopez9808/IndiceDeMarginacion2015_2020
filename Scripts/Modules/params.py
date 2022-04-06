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
                         "color": "#b7094c",
                         },
            'Bajo': {"id": 1,
                     "color": "#892b64",
                     },
            'Medio': {"id": 2,
                      "color": "#5c4d7d",
                      },
            'Alto': {"id": 3,
                     "color": "#2e6f95",
                     },
            'Muy alto': {"id": 4,
                         "color": "#0091ad",
                         },
        },
        # Parametros para el método de PCA
        "PCA": {
            "kernels": {
                "linear": {"elevation": 19},
                "rbf": {"elevation": 0},
                "cosine": {"elevation": 0},
                "sigmoid": {"elevation": 0}
            },
            "2D": {"components": 2,
                   "file results": "PCA_2D.csv",
                   "file graphics": "PCA_2D.png"},
            "3D": {"components": 3,
                   "file animation format": "PCA_3D_{}",
                   "file results": "PCA_3D.csv"},
        },
        "ISOMAP": {
            "neighbors": {8: {"elevation": 34},
                          10: {"elevation": 34},
                          12: {"elevation": 34},
                          14: {"elevation": 34}},
            "2D": {"components": 2,
                   "file graphics": "ISOMAP_2D.png",
                   "file results": "ISOMAP_2D.csv"},
            "3D": {"components": 3,
                   "file animation format": "ISOMAP_3D_{}",
                   "file results": "ISOMAP_3D.csv"},
        },
        "TSNE": {
            "perplexity": {
                100: {"elevation": 0},
                200: {"elevation": 0},
                300: {"elevation": 0},
                400: {"elevation": 0}
            },
            "2D": {"components": 2,
                   "file results": "TSNE_2D.csv",
                   "file graphics": "TSNE_2D.png"},
            "3D": {"components": 3,
                   "file animation format": "TSNE_3D_{}",
                   "file results": "TSNE_3D.csv"},
        },
        "LLE":
        {
            "neighbors": [4, 5, 6, 7],
            "2D": {"components": 2,
                   "filenane": "LLE_2D.csv"},
            "3D": {"components": 3,
                   "filenane": "LLE_3D.csv"},
        },
        "Kmeans": {
            "k-means++",
            "random",
        }
    }
    params["SOM colors"] = _define_SOM_colors(params)
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


def _define_SOM_colors(params: dict) -> dict:
    colors = {}
    for classes in params["classes"]:
        dataset = params["classes"][classes]
        id = dataset["id"]
        color = dataset["color"]
        colors[id] = color
    return colors


def define_filenames_2D(params: dict, model: str) -> dict:
    params["file graphics"] = params[model]["2D"]["file graphics"]
    params = define_file_results(params, model, "2D")
    return params


def define_filenames_3D(params: dict, model: str) -> dict:
    params = define_file_results(params, model, "3D")
    return params


def define_file_results(params: dict, model: str, dim: str) -> dict:
    params["file results"] = params[model][dim]["file results"]
    return params


def define_file_animation(dataset: dict, param: str) -> str:
    filename = dataset["3D"]["file animation format"].format(param)
    return filename
