from Modules.data_model import data_class
from Modules.params import get_params
from Modules.som import SOM_model

years = [2015, 2020]
for year in years:
    print("-"*30)
    print("Analizando año {}".format(year))
    params = get_params(year)
    params["file results"] = "SOM.csv"
    data = data_class(params)
    som = SOM_model()
    som.run(data.embedding)
    vector = som.get_results()
    data.add_results(vector,
                     som.name)
    data.save_results(params["file results"])
