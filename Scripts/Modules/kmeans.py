"""
Clase que contiene la ejecucion y organización de resultados del algortimo KMeans
"""

from sklearn.cluster import KMeans
from numpy import array


class kmeans_model:
    def __init__(self) -> None:
        pass

    def create(self, init: str) -> None:
        """
        Inicializa el modelo ISOMAP dado el nombre del inicializador
        """
        self.model = KMeans(n_clusters=5,
                            init=init)
        self._generate_header_name(init)

    def run(self, data: array) -> None:
        """
        Ejecuta el modelo KMeans dado un embedding
        """
        self.model_results = self.model.fit(data)
        self.results = self.model_results.predict(data)
        self.results = self.results.reshape((-1, 1))

    def get_results(self) -> array:
        """
        Regresa los resultados del algoritmo en forma de array
        """
        return self.results.copy()

    def _generate_header_name(self, init: str) -> array:
        """
        Genera el nombre de los headers para guardar los datos
        """
        self.name = [init]
