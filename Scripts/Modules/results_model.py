from pandas import DataFrame, read_csv
from os.path import join
from numpy import array


class results_model:
    def __init__(self, params: dict) -> None:
        self.params = params
        self.read()

    def read(self) -> DataFrame:
        filename = join(self.params["path results"],
                        self.params["file results"])
        self.data = read_csv(filename,
                             index_col=0)

    def add_results(self, data: array, name: list) -> None:
        self.data[name] = data

    def save_results(self, filename):
        filename = join(self.params["path results"],
                        filename)
        self.data.to_csv(filename)
