from sklearn.decomposition import KernelPCA
from numpy import array


class PCA_model:
    def __init__(self) -> None:
        pass

    def create(self, n_components: int, kernel: str) -> None:
        self.model = KernelPCA(n_components,
                               kernel=kernel,
                               degree=2
                               )
        self.generate_header_names(n_components)

    def run(self, data: array) -> None:
        self.model.fit(data)

    def generate_header_names(self, n_components: int) -> array:
        name = "Component {}"
        self.names = [name.format(i+1)
                      for i in range(n_components)]

    def get_eigenvectors(self) -> array:
        return self.model.eigenvectors_

    def get_eigenvalues(self) -> array:
        return self.model.eigenvalues_
