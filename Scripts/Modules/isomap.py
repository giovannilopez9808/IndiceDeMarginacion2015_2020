"""
Clase que contiene la ejecucion y organización de resultados del algortimo ISOMAP
"""

from sklearn.manifold import Isomap
from numpy import array


class isomap_model:
    def __init__(self) -> None:
        pass

    def create(self, neighbors: int, components: int) -> None:
        """
        Inicializa el modelo ISOMAP dado el numero de componentes y numero de vecinos a tomar
        """
        self.model = Isomap(n_neighbors=neighbors,
                            n_components=components)
        self.generate_header_names(components, neighbors)

    def generate_header_names(self, n_components: int, neighbors: str) -> array:
        """
        Genera el nombre de los headers para guardar los datos
        """
        name = "Neighbors {} Component {}"
        self.names = [name.format(neighbors, i+1)
                      for i in range(n_components)]

    def run(self, data: array) -> array:
        """
        Ejecuta el modelo ISOMAP dado un embedding
        """
        self.model.fit(data)
        self.results = self.model.transform(data)

    def get_results(self) -> array:
        """
        Resultados del la ejecucción del modelo
        """
        return self.results.copy()
