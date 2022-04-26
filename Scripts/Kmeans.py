from Modules.data_model import data_class
from Modules.kmeans import kmeans_model
from Modules.params import get_params

years = [2015, 2020]
for year in years:
    print("-"*30)
    print("Analizando año {}".format(year))
    params = get_params(year)
    data = data_class(params)
    kmeans = kmeans_model()
    for init in params["Kmeans"]:
        filename = "kmeans_{}.csv".format(init)
        params["file results"] = filename
        kmeans.create(init)
        kmeans.run(data.embedding)
        vector = kmeans.get_results()
        data.add_results(vector,
                         kmeans.name)
        data.save_results(params["file results"])
