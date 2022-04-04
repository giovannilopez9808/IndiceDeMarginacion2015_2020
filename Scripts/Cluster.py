from Modules.cluster_model import cluster_class
from Modules.data_model import data_class
from Modules.params import get_params

params = get_params()
params["file results"] = "Cluster.csv"
data = data_class(params)
som = cluster_class()
som.run(data.embedding)
vector = som.get_results()
data.add_results(vector,
                 som.name)
data.save_results(params["file results"])
