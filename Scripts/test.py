from Modules.data_model import data_class
from Modules.map_model import map_model
from Modules.params import get_params

params = get_params()
data = data_class(params)
map = map_model(params)
map.merge(data)
map.plot_GM()
