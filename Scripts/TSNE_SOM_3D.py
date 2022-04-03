"""
Analisis de los datos usando el método de isomap en el caso de dos dimensiones

Genera una gráfica y animacion con la visualziacion de los puntos en 3D y guarda los eigenvectores resultantes en un archivo.
"""

from Modules.data_model import data_class, join
from Modules.results_model import results_model
from Modules.animation import create_animation
from Modules.params import get_params, mkdir
from Modules.tsne import TSNE_model
import matplotlib.pyplot as plt

# Lectura de los parametros
params = get_params()
params["file results"] = "TSNE_3D.csv"
# Lectura de los datos
data = data_class(params)
# Inicializacion del modelo
tsne = TSNE_model()
tsne_results = results_model(params)
params["file results"] = "SOM.csv"
som_results = results_model(params)
colors = [params["SOM colors"][value]
          for value in som_results.data["SOM labels"]]
# Resultados
for perplexity in params["TSNE"]["perplexity"]:
    print("Analizando datos con perplexitys = {}".format(perplexity))
    # Nombre y parametros del plot
    params["file animation"] = "tsne_som_3D_{}".format(
        str(perplexity).zfill(2))
    # tsne file results name
    params["path pictures"] = join(params["path graphics"],
                                   params["file animation"])
    mkdir(params["path pictures"])
    elevation = params["TSNE"]["perplexity"][perplexity]["elevation"]
    tsne.create(params["TSNE"]["3D"]["components"],
                perplexity)
    subresults = tsne_results.data[tsne.names].to_numpy()
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(subresults[:, 0],
               subresults[:, 1],
               subresults[:, 2],
               alpha=0.5,
               c=colors,)
    plt.axis("off")
    plt.legend(ncol=len(data.classes),
               frameon=False,
               loc="upper center",
               fontsize=12)
    plt.tight_layout()
    plt.show()
    # Guardado de cada angulo
#     for i, angle in enumerate(range(-180, 181)):
#         ax.view_init(elevation, angle)
#         filename = "isomap_{}".format(str(i).zfill(3))
#         filename = join(params["path pictures"],
#                         filename)
#         plt.savefig(filename)
#     # Creacion de la animacion
#     create_animation(params["path graphics"],
#                      params["path pictures"],
#                      params["file animation"],
#                      delete=False,
#                      fps=30)
# data.save_results(params["file results"])
