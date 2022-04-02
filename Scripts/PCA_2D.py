"""
Analisis de los datos usando el método de PCA en el caso de dos dimensiones

Genera una gráfica con la visualziacion de los puntos en 2D y guarda los eigenvalores resultantes en un archivo.
"""

from Modules.data_model import data_class, join
from Modules.params import get_params
from Modules.models import PCA_model
import matplotlib.pyplot as plt
from numpy import array

# Lectura de los parametros
params = get_params()
# PCA file results name
params["file graphics"] = "PCA_2D.png"
# PCA file graphics name
params["file results"] = "PCA_2D.csv"
# Lectura de los datos
data = data_class(params)
# Inicializacion del modelo
pca = PCA_model()
pca.create(params["PCA"]["2D"]["components"],
           params["PCA"]["2D"]["kernel"])
# Calculo de PCA
pca.run(data.embedding)
# Resultados
vectors = pca.get_eigenvectors()
data.add_results(vectors,
                 pca.names)
data.save_results(params["file results"])
plt.subplots(figsize=(12, 8))
# Ploteo de cada clase
for classes in data.classes:
    index = data.data_2020["GM"] == classes
    index = array(data.data_2020.index[index])
    color = data.classes[classes]["color"]
    subset = vectors[index]
    plt.scatter(subset[:, 0],
                subset[:, 1],
                alpha=0.5,
                c=color,
                label=classes)
plt.axis("off")
plt.tight_layout(pad=2)
plt.legend(ncol=len(data.classes),
           bbox_to_anchor=(0.75, 1.025))
# Guardado de cada grafica
filename = join(params["path graphics"],
                params["file graphics"])
plt.savefig(filename,
            dpi=300)
