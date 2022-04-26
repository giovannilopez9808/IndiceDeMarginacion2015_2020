from Modules.params import get_params, get_metrics_params
from Modules.metrics_model import metrics_class
from Modules.results_model import results_model
from Modules.data_model import data_class
from pandas import DataFrame
from os.path import join

params = get_params()
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
