"""
Analisis de los datos usando el método de PCA en el caso de dos dimensiones

Genera una gráfica con la visualziacion de los puntos en 2D y guarda los eigenvalores resultantes en un archivo.
"""

from Modules.params import define_filenames_2D, get_params
from Modules.data_model import data_class, join
from Modules.pca import PCA_model
import matplotlib.pyplot as plt

years = [2015, 2020]

for year in years:
    print("-"*30)
    print("Analizando año {}".format(year))
    # Lectura de los parametros
    params = get_params(year)
    model_name = "PCA"
    # Definicion de los archivos resultantes
    params = define_filenames_2D(params,
                                 model_name)
    dataset = params[model_name]
    # Lectura de los datos
    data = data_class(params)
    # Inicializacion del modelo
    pca = PCA_model()
    # Resultados
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs = axs.flatten()
    for ax, kernel in zip(axs, dataset["kernels"]):
        pca.create(dataset["2D"]["components"],
                   kernel)
        # Calculo de PCA
        pca.run(data.embedding)
        vectors = pca.get_eigenvectors()
        data.add_results(vectors,
                         pca.names)
        # Ploteo de cada clase
        ax.set_title(kernel)
        for classes in data.classes:
            index = data.obtain_index_data_for_class(classes)
            color = data.obtain_color_classes(classes)
            subset = vectors[index]
            ax.scatter(subset[:, 0],
                       subset[:, 1],
                       alpha=0.5,
                       c=color,
                       label=classes)
            ax.axis("off")
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels,
               title="Índice de marginación",
               frameon=False,
               ncol=len(data.classes),
               bbox_to_anchor=(0.75, 1))
    plt.tight_layout(pad=4)
    # Guardado de cada grafica
    filename = join(params["path graphics"],
                    params["file graphics"])
    plt.savefig(filename,
                dpi=300)
    data.save_results(params["file results"])
