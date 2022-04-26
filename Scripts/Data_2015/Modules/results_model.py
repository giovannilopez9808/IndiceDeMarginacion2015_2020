from pandas import DataFrame, read_csv
from os.path import join
from numpy import array


class results_model:
    def __init__(self, params: dict) -> None:
        self.params = params
        self.read()
        self._get_id_class()

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

    def _get_id_class(self) -> None:
        self.data["id"] = self.data["GM"].apply(lambda x:
                                                self.params["classes"][x]["id"])

    def get_id_labels(self) -> array:
        id_labels = self.get_column_data("id")
        return id_labels

    def get_column_data(self, column_name: str) -> array:
        data = self.data[column_name].to_numpy()
        return data
