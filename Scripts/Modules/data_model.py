"""
Clase que lee y organiza los datos para el guardado de los resultados y obtener diferentes parametros obtenidos del dataset. Las funciones que son para uso unico dentro de la clase tienen un guion bajo al inicio de su nombre
"""

from pandas import DataFrame, Series, read_csv
from numpy import array, mean, std
from os.path import join


class data_class:
    def __init__(self, params: dict) -> None:
        """
        Lectura y almacenamiento de los datos 

        Input
        ----------------
        params: diccionario con las rutas y nombres de los archivos
        """
        self._embedding_columns = params["embedding columns"]
        self._useless_colums = params["useless columns"]
        self.classes = params["classes"]
        self.params = params
        self.read()

    def read(self) -> None:
        """
        Ejecucción de las lecturas de los archivos a analizar
        """
        self.read_dictionary()
        self.read_data()

    def read_dictionary(self) -> dict:
        """
        Lectura del diccionario de siglas de los datos
        """
        # Nombre del archivo
        filename = join(self.params["path data"],
                        self.params["file dictionary"])
        # Lectura del archivo
        self.dictonary = read_csv(filename,
                                  index_col=0)
        # Transformación a diccinario
        dictionary = {}
        for index in self.dictonary.index:
            dictionary[index] = self.dictonary["Descripción"][index]
        # Guardado el diccionario
        self.dictonary = dictionary

    def read_data(self) -> DataFrame:
        """
        Lectura de los archivos de datos de 1990 a 2020
        """
        self.data_1990 = self.read_file(self.params["path data"],
                                        self.params["file data 1990"],
                                        "latin-1")
        self.data_2020 = self.read_file(self.params["path data"],
                                        self.params["file data 2020"],
                                        "utf-8")
        self._obtain_index_town()
        self._obtain_index_state()
        self._clean_data()
        self._classify_with_GM_column()
        self._obtain_embedding()
        self._initialize_results_dataframe()

    def read_file(self, path: str, name: str, encoding: str) -> DataFrame:
        """
        Lectura estandarizada de los datos
        """
        filename = join(path,
                        name)
        data = read_csv(filename,
                        encoding=encoding,)
        return data

    def _classify_with_GM_column(self) -> None:
        self.data_2020["classes"] = self.data_2020["GM"].apply(
            lambda x: self.classes[x]["id"])

    def _obtain_index_town(self) -> dict:
        """
        Creacion de un diccionario del nombre de cada municipio
        """
        index_town = {}
        for i in self.data_2020.index:
            index = self.data_2020["CVE_MUN"][i]
            town = self.data_2020["NOM_MUN"][i]
            index_town[index] = town
        self.index_town = index_town

    def _obtain_index_state(self):
        """
        Creacion de un diccionario del nombre de cada estado
        """
        index_state = {}
        for i in self.data_2020.index:
            index = self.data_2020["CVE_ENT"][i]
            state = self.data_2020["NOM_ENT"][i]
            index_state[index] = state
        self.index_state = index_state

    def _clean_data(self):
        """
        Limpieza de las columnas que no seran utilizadas
        """
        self.data_1990 = self.data_1990.drop(columns=self._useless_colums)
        self.data_2020 = self.data_2020.drop(columns=self._useless_colums)

    def _obtain_embedding(self) -> array:
        """
        Creacion de la matriz de embeddings para realizar sus analisis
        """
        embedding = DataFrame()
        for column in self._embedding_columns:
            embedding[column] = self.data_2020[column]
        self.embedding = embedding.to_numpy()
        mu = mean(self.embedding, axis=0)
        sigma = std(self.embedding, axis=0)
        self.embedding = (self.embedding-mu)/sigma

    def _initialize_results_dataframe(self) -> DataFrame:
        self.results = DataFrame()
        self.results["CVE_MUN"] = self.data_2020["CVE_MUN"]
        self.results["GM"] = self.data_2020["GM"]
        self.results["IM"] = self.data_2020["IM"]
        self.results["IMN"] = self.data_2020["IMN"]

    def obtain_index_data_for_class(self, classes: str) -> DataFrame:
        """
        Obtiene los indices de la clase de dato seleccionada
        """
        return self.data_2020["GM"] == classes

    def obtain_color_classes(self, classes: str) -> str:
        """
        Obtiene el color de la clase seleccionada
        """
        return self.classes[classes]["color"]

    def obtain_frecuency_clasees(self) -> Series:
        return self.data_2020["GM"].value_counts()

    def add_results(self, data: array, names: list) -> None:
        """
        Añadir vectores de resultados a los creados anteriormente
        """
        n = len(names)
        for i in range(n):
            values = data[:, i]
            name = names[i]
            self.results[name] = values

    def save_results(self, filename: str):
        """
        Guardado de lso resultados en la ruta señalada en los parametros dados y el nombre ingresado
        """
        filename = join(self.params["path results"],
                        filename)
        self.results.to_csv(filename,
                            index=False)
