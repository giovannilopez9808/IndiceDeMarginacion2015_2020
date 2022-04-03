"""
Analisis de los datos usando el método de isomap en el caso de dos dimensiones

Genera una gráfica con la visualziacion de los puntos en 2D y guarda los eigenvalores resultantes en un archivo.
"""

from sklearn import neighbors
from Modules.data_model import data_class, join
from Modules.params import get_params
from Modules.isomap import isomap_model
import matplotlib.pyplot as plt

# Lectura de los parametros
params = get_params()
# isomap file results name
params["file graphics"] = "ISOMAP_2D.png"
# isomap file graphics name
params["file results"] = "ISOMAP_2D.csv"
# Lectura de los datos
data = data_class(params)
# Inicializacion del modelo
isomap = isomap_model()
# Calculo de isomap
# Resultados
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.flatten()
for ax, neighbor in zip(axs, params["isomap"]["2D"]["neighbors"]):
    isomap.create(neighbor,
                  params["isomap"]["2D"]["components"])
    isomap.run(data.embedding)
    vectors = isomap.get_results()
    data.add_results(vectors,
                     isomap.names)
    # Ploteo de cada clase
    ax.set_title("Neighbors = {}".format(neighbor))
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
plt.tight_layout(pad=3)
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels,
           frameon=False,
           ncol=len(data.classes),
           bbox_to_anchor=(0.75, 1.01))
# Guardado de cada grafica
filename = join(params["path graphics"],
                params["file graphics"])
plt.savefig(filename,
            dpi=300)
data.save_results(params["file results"])
