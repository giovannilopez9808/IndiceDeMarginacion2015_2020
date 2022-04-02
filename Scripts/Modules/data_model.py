from pandas import DataFrame, read_csv
from os.path import join


class data_class:
    def __init__(self, params: dict) -> None:
        """
        Lectura y almacenamiento de los datos 

        Input
        ----------------
        params: diccionario con las rutas y nombres de los archivos
        """
        self.params = params
        self.read()

    def read(self) -> None:
        """
        Ejecucción de las lecturas de los archivos a analizar
        """
        self.read_dictionary()
        self.read_data()

    def read_dictionary(self) -> None:
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

    def read_data(self) -> None:
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

    def read_file(self, path: str, name: str, encoding: str) -> DataFrame:
        """
        Lectura estandarizada de los datos
        """
        filename = join(path,
                        name)
        data = read_csv(filename,
                        encoding=encoding)
        return data

    def _obtain_index_town(self):
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
