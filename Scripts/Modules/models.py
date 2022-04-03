from sklearn.manifold import LocallyLinearEmbedding, Isomap, TSNE
from sklearn.cluster import AgglomerativeClustering
from sklearn.manifold import Isomap
from pandas import DataFrame
from somlearn import SOM
from numpy import array


class SOM_model_class:

    def __init__(self) -> None:
        self.obtain_index_plot_animals()

    def run(self, data: array) -> DataFrame:
        model = SOM(n_columns=2, n_rows=2, random_state=1)
        self.results = model.fit_predict(data)

    def obtain_index_plot_animals(self):
        self.animals_index = range(50)

    def create_classes_dataframe(self, names: array) -> DataFrame:
        self.classes = DataFrame(names, columns=["Names"])
        self.classes["SOM"] = self.results
        self.classes.index = self.classes["Names"]
        self.classes = self.classes.drop(columns="Names")


class cluster_model_class():

    def __init__(self) -> None:
        pass

    def run(self, data: array, clusters: int, linkage: str):
        clustering = AgglomerativeClustering(n_clusters=clusters,
                                             linkage=linkage)
        self.results = clustering.fit_predict(data)

    def create_classes_dataframe(self, names: array) -> DataFrame:
        self.classes = DataFrame(names, columns=["Names"])
        self.classes["Classes"] = self.results
        self.classes.index = self.classes["Names"]
        self.classes = self.classes.drop(columns="Names")
