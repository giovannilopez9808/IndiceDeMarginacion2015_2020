"""
Analisis de los datos usando el método de PCA en el caso de dos dimensiones

Genera una gráfica y animacion con la visualziacion de los puntos en 3D y guarda los eigenvectores resultantes en un archivo.
"""

from Modules.data_model import data_class, join
from Modules.animation import create_animation
from Modules.params import get_params, mkdir
from Modules.models import PCA_model
import matplotlib.pyplot as plt

# Lectura de los parametros
params = get_params()
params["file animation"] = "PCA_3D"
params["file results"] = "PCA_3D.csv"
# PCA file results name
params["path pictures"] = join(params["path graphics"],
                               params["file animation"])
mkdir(params["path pictures"])
# PCA file graphics name
# Lectura de los datos
data = data_class(params)
# Inicializacion del modelo
pca = PCA_model()
pca.create(params["PCA"]["3D"]["components"],
           params["PCA"]["3D"]["kernel"])
# Calculo de PCA
pca.run(data.embedding)
# Resultados
vectors = pca.get_eigenvectors()
data.add_results(vectors,
                 pca.names)
data.save_results(params["file results"])
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')
# Ploteo de cada clase
for classes in data.classes:
    index = data.data_2020["GM"] == classes
    color = data.classes[classes]["color"]
    subset = vectors[index]
    ax.scatter(subset[:, 0],
               subset[:, 1],
               subset[:, 2],
               alpha=0.5,
               c=color,
               label=classes)
plt.axis("off")
plt.legend(ncol=len(data.classes),
           bbox_to_anchor=(0.82, 1),
           fontsize=12)
plt.tight_layout()
# Guardado de cada angulo
for i, angle in enumerate(range(-180, -170)):
    ax.view_init(34, angle)
    filename = "PCA_{}".format(str(i).zfill(3))
    filename = join(params["path pictures"],
                    filename)
    plt.savefig(filename)
# Creacion de la animacion
create_animation(params["path graphics"],
                 params["path pictures"],
                 "PCA_3D",
                 delete=False,
                 fps=30)
