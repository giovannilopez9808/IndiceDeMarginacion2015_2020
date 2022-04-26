"""
Clase que contiene la estructura para la ejecuccion del modelo de TSNE para diferentes datos dado el número de componentes y perplejidad
"""

from somlearn import SOM
from numpy import array


class SOM_model:
    def __init__(self) -> None:
        self._create()

    def _create(self) -> None:
        """
        Inicializa el modelo PCA dado el numero de componentes y el nombre del kernel
        """
        self.model = SOM(n_rows=1,
                         n_columns=5)
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
        self.name = ["SOM labels"]

    def get_results(self) -> array:
        """
        Resultados del la ejecucción del modelo
        """
        return self.results.copy()
