"""
Calculo de metricas a los resultados obtenidos de los algoritmos SOM, KMeans y Hierachical Cluster

Se obtiene una tabla por cada algoritmo mostrando las metricas y una grafica donde se visualiza la tabla de confusion
"""

from Modules.params import get_params, get_metrics_params
from Modules.metrics_model import metrics_class
from Modules.results_model import results_model
from Modules.data_model import data_class
from pandas import DataFrame
from os.path import join

years = [2015, 2020]
for year in years:
    print("-"*30)
    print("Analizando año {}".format(year))
    params = get_params(year)
    datasets = get_metrics_params()
    data = data_class(params)
    metrics = metrics_class(params,
                            data.embedding)
    results = {}
    for model_name in datasets["Models"]:
        dataset = datasets["Models"][model_name]
        params["file graphics"] = dataset["file graphics"]
        params["file results"] = dataset["filename"]
        params["model name"] = model_name
        model_results = results_model(params)
        model = dataset["class"]
        model = model()
        label = dataset["label"]
        true_labels = model_results.get_id_labels()
        model_labels = model_results.get_column_data(label)
        results[model_name] = metrics.apply_all_metrics(true_labels,
                                                        model_labels)
    results = DataFrame(results)
    results.index.name = "Metrics"
    params["file results"] = "metrics.csv"
    filename = join(params["path results"],
                    params["file results"])
    results.to_csv(filename)
