from pandas import DataFrame, read_csv
from os.path import join
from numpy import array


class results_model:
    """
    Modelo para guardar los resultados de cada modelo creado
    """

    def __init__(self, params: dict) -> None:
        self.params = params
        self._read()
        self._get_id_class()

    def _read(self) -> DataFrame:
        """
        Lectura de los resultados del modelo
        """
        filename = join(self.params["path results"],
                        self.params["file results"])
        self.data = read_csv(filename,
                             index_col=0)

    def add_results(self, data: array, name: list) -> None:
        """
        Añadimos una columna de resultados
        """
        self.data[name] = data

    def save_results(self, filename):
        """
        Guardado del archivo de resultados
        """
        filename = join(self.params["path results"],
                        filename)
        self.data.to_csv(filename)

    def _get_id_class(self) -> None:
        """
        Obtiene el ID de cada clase de los datos
        """
        self.data["id"] = self.data["GM"].apply(lambda x:
                                                self.params["classes"][x]["id"])

    def get_id_labels(self) -> array:
        """
        Regresa la columna de id de los datos
        """
        id_labels = self.get_column_data("id")
        return id_labels

    def get_column_data(self, column_name: str) -> array:
        """
        Regresa una columna de datos dado el nombre de la columna
        """
        data = self.data[column_name].to_numpy()
        return data
