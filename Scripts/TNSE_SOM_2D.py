from Modules.results_model import results_model, join
from Modules.data_model import data_class
from Modules.params import get_params
from Modules.tsne import TSNE_model
import matplotlib.pyplot as plt

params = get_params()
params["file graphics"] = "TSNE_SOM_2D.png"
params["file results with SOM"] = "TSNE_SOM_2D.csv"
params["file results"] = "TSNE_2D.csv"
tsne_results = results_model(params)
params["file results"] = "SOM.csv"
SOM_results = results_model(params)
data = data_class(params)
colors = [params["SOM colors"][value]
          for value in SOM_results.data["SOM labels"]]
tsne = TSNE_model()
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.flatten()
for ax, perplexity in zip(axs, params["TSNE"]["perplexity"]):
    tsne.create(params["TSNE"]["2D"]["components"],
                perplexity)
    subresults = tsne_results.data[tsne.names].to_numpy()
    # Ploteo de cada clase
    ax.set_title("perplexitys = {}".format(perplexity))
    ax.scatter(subresults[:, 0],
               subresults[:, 1],
               alpha=0.5,
               c=colors,
               cmap="Set1")
    ax.axis("off")
plt.tight_layout(pad=3)
# Guardado de cada grafica
filename = join(params["path graphics"],
                params["file graphics"])
plt.savefig(filename,
            dpi=300)
