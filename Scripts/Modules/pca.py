"""
Clase que contiene la estructura para la ejecuccion del algoritmo de PCA para diferentes datos dado el número de componentes a obtener y el nombre del kernel
"""

from sklearn.decomposition import KernelPCA
from numpy import array


class PCA_model:
    def __init__(self) -> None:
        pass

    def create(self, n_components: int, kernel: str) -> None:
        """
        Inicializa el algoritmo PCA dado el numero de componentes y el nombre del kernel
        """
        self.model = KernelPCA(n_components,
                               kernel=kernel,
                               )
        self.generate_header_names(n_components, kernel)

    def run(self, data: array) -> None:
        """
        Ejecuta el algoritmo PCA dado un embedding
        """
        self.model.fit(data)

    def generate_header_names(self, n_components: int, kernel: str) -> array:
        """
        Genera el nombre de los headers para guardar los datos
        """
        name = "{} Component {}"
        self.names = [name.format(kernel, i+1)
                      for i in range(n_components)]

    def get_eigenvectors(self) -> array:
        """
        Obtiene los eigenvectores de los resultados de PCA
        """
        return self.model.eigenvectors_

    def get_eigenvalues(self) -> array:
        """
        Obtiene los eigenvalores de los resultados de PCA
        """
        return self.model.eigenvalues_
