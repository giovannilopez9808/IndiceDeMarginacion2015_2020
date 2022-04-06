"""
Analisis de los datos usando el método de isomap en el caso de dos dimensiones

Genera una gráfica y animacion con la visualziacion de los puntos en 3D y guarda los eigenvectores resultantes en un archivo.
"""

from Modules.params import get_params, mkdir, define_file_animation, define_filenames_3D
from Modules.data_model import data_class, join
from Modules.animation import create_animation
from Modules.tsne import TSNE_model
import matplotlib.pyplot as plt

# Lectura de los parametros
params = get_params()
model_name = "TSNE"
params = define_filenames_3D(params,
                             model_name)
dataset = params[model_name]
# Lectura de los datos
data = data_class(params)
# Inicializacion del modelo
tsne = TSNE_model()
# Resultados
for perplexity in dataset["perplexity"]:
    print("Analizando datos con perplexitys = {}".format(perplexity))
    # Nombre y parametros del plot
    params["file animation"] = define_file_animation(dataset,
                                                     perplexity)
    # tsne file results name
    params["path pictures"] = join(params["path graphics"],
                                   params["file animation"])
    mkdir(params["path pictures"])
    elevation = dataset["perplexity"][perplexity]["elevation"]
    tsne.create(dataset["3D"]["components"],
                perplexity)
    # Calculo de tsne
    tsne.run(data.embedding)
    vectors = tsne.get_results()
    data.add_results(vectors,
                     tsne.names)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')
    # Ploteo de cada clase
    for classes in data.classes:
        index = data.obtain_index_data_for_class(classes)
        color = data.obtain_color_classes(classes)
        subset = vectors[index]
        ax.scatter(subset[:, 0],
                   subset[:, 1],
                   subset[:, 2],
                   alpha=0.5,
                   c=color,
                   label=classes)
    plt.axis("off")
    plt.legend(ncol=len(data.classes),
               title="Índice de marginación",
               frameon=False,
               loc="upper center",
               fontsize=12)
    plt.tight_layout()
    # Guardado de cada angulo
    for i, angle in enumerate(range(-180, 181)):
        ax.view_init(elevation, angle)
        filename = "TSNE_{}".format(str(i).zfill(3))
        filename = join(params["path pictures"],
                        filename)
        plt.savefig(filename)
    # Creacion de la animacion
    create_animation(params["path graphics"],
                     params["path pictures"],
                     params["file animation"],
                     delete=False,
                     fps=30)
data.save_results(params["file results"])
