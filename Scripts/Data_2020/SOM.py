from Modules.data_model import data_class
from Modules.params import get_params
from Modules.som import SOM_model

params = get_params()
params["file results"] = "SOM.csv"
data = data_class(params)
som = SOM_model()
som.run(data.embedding)
vector = som.get_results()
data.add_results(vector,
                 som.name)
data.save_results(params["file results"])
