from Modules.data_model import data_class
from Modules.map_model import map_model
from Modules.params import get_params

years = [2015, 2020]
for year in years:
    print("-"*30)
    print("Analizando año {}".format(year))
    params = get_params(year)
    params["file map"] = "map.png"
    data = data_class(params)
    map = map_model(params)
    map.merge(data)
    map.plot_GM()
