from Modules.metrics_model import metrics_class
from Modules.results_model import results_model
from Modules.cluster_model import cluster_class
from Modules.data_model import data_class
from Modules.kmeans import kmeans_model
from Modules.params import get_params
from Modules.som import SOM_model
from pandas import DataFrame

datasets = {
    "Models": {
        "SOM": {
            "filename": "SOM.csv",
            "file graphics": "SOM_confusion_matrix.png",
            "class": SOM_model,
        },
        "Cluster": {
            "filename": "Cluster.csv",
            "file graphics": "Cluster_confusion_matrix.png",
            "class": cluster_class,
        },
        "Kmeans++": {
            "filename": "Kmeans.csv",
            "file graphics": "Kmeans++_confusion_matrix.png",
            "class": kmeans_model,
            "label": "k-means++"
        },
        "Kmeans": {
            "filename": "Kmeans.csv",
            "file graphics": "Kmeans_random_confusion_matrix.png",
            "class": kmeans_model,
            "label": "random"
        },
    }
}

params = get_params()
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
    if "Kmeans" in model_name:
        label = dataset["label"]
    else:
        label = model.name[0]
    true_labels = model_results.get_id_labels()
    model_labels = model_results.get_column_data(label)
    results[model_name] = metrics.apply_all_metrics(true_labels,
                                                    model_labels)
results = DataFrame(results)
print(results)
