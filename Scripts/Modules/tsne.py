"""
Clase que contiene la estructura para la ejecuccion del modelo de TSNE para diferentes datos dado el número de componentes y perplejidad
"""

from sklearn.manifold import TSNE
from numpy import array


class TSNE_model:
    def __init__(self) -> None:
        pass

    def create(self, n_components: int, perplexity: int) -> None:
        """
        Inicializa el modelo PCA dado el numero de componentes y el nombre del kernel
        """
        self.model = TSNE(n_components=n_components,
                          perplexity=perplexity,
                          random_state=12345,
                          init="pca",
                          learning_rate="auto")
        self.generate_header_names(n_components)

    def run(self, data: array) -> None:
        """
        Ejecuta el modelo PCA dado un embedding
        """
        self.results = self.model.fit_transform(data)

    def generate_header_names(self, n_components: int) -> array:
        """
        Genera el nombre de los headers para guardar los datos
        """
        name = "Component {}"
        self.names = [name.format(i+1)
                      for i in range(n_components)]

    def get_results(self) -> array:
        """
        Resultados del la ejecucción del modelo
        """
        return self.results.copy()
