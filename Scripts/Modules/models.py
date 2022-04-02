from sklearn.decomposition import PCA
from numpy import array


class PCA_model:
    def __init__(self) -> None:
        pass

    def create(self, n_components: int) -> None:
        self.model = PCA(n_components)

    def run(self, data: array) -> None:
        self.model.fit(data)
