from Modules.data_model import data_class
from Modules.params import get_params

params = get_params()
data = data_class(params)
print(data.data_1990)
print(data.data_2020)
