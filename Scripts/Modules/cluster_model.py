"""
Clase que contiene la logica y organización de comandos de ejecuccion para el algoritmo Hierachical Cluster
"""

from sklearn.cluster import AgglomerativeClustering
from numpy import array


class cluster_class():

    def __init__(self) -> None:
        self.create()

    def create(self) -> None:
        """
        Inicializa el modelo PCA dado el numero de componentes y el nombre del kernel
        """
        self.model = AgglomerativeClustering(n_clusters=5,
                                             linkage="complete",
                                             affinity="cosine")
        self._generate_header_name()

    def run(self, data: array) -> None:
        """
        Ejecuta el modelo PCA dado un embedding
        """
        self.results = self.model.fit_predict(data)
        self.results = self.results.reshape((-1, 1))

    def _generate_header_name(self) -> array:
        """
        Genera el nombre de los headers para guardar los datos
        """
        self.name = ["Cluster labels"]

    def get_results(self) -> array:
        """
        Resultados del la ejecucción del modelo
        """
        return self.results.copy()
