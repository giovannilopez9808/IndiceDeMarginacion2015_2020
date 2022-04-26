from numpy import array
from sklearn.cluster import KMeans


class kmeans_model:
    def __init__(self) -> None:
        pass

    def create(self, init: str) -> None:
        self.model = KMeans(n_clusters=5,
                            init=init)
        self._generate_header_name(init)

    def run(self, data: array) -> None:
        self.model_results = self.model.fit(data)
        self.results = self.model_results.predict(data)
        self.results = self.results.reshape((-1, 1))

    def get_results(self) -> array:
        return self.results.copy()

    def _generate_header_name(self, init: str) -> array:
        """
        Genera el nombre de los headers para guardar los datos
        """
        self.name = [init]
