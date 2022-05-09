"""
Programa para crear mapas de México tomando en cuenta el indice de marginación
"""

from geopandas import read_file, GeoDataFrame
from .data_model import data_class, join
from .params import get_classes_colors
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt


class map_model:
    """
    Modelo para generar la gráfica del mapa de México 
    """

    def __init__(self, params: dict) -> None:
        """
        Constructor
        """
        self.params = params
        self.read()

    def read(self) -> GeoDataFrame:
        """
        Lectura de los datos
        """
        self.data = read_file(self.params["path map"])
        # Estandarización del nombre del indice de cada municipio
        self.data = self.data.rename(columns={"CLAVE": "CVE_MUN"})

    def merge(self, data: data_class) -> GeoDataFrame:
        """
        Concadenación de los datos por medio del índice de municipio
        """
        self.data = self.data.merge(data.data,
                                    on="CVE_MUN")

    def plot_GM(self) -> None:
        """
        Ploteo del GM sobre el mapa dado
        """
        colors = get_classes_colors(self.params)
        self.data["color"] = self.data["GM"].apply(
            lambda x: self.params["classes"][x]["color"])
        fig, ax = plt.subplots(figsize=(12, 8))
        self.data.plot(
            column='GM',
            legend=True,
            color=self.data["color"],
            ax=ax,
        )
        custom_points = [Line2D([0], [0],
                                marker="o",
                                linestyle="none",
                                markersize=5,
                                color=color)
                         for color in colors.values()]
        leg_points = ax.legend(custom_points,
                               colors.keys(),
                               title="Índice de marginación",
                               frameon=False,
                               ncol=5,
                               loc=(0.3, 0.96))
        ax.add_artist(leg_points)
        ax.axis("off")
        plt.tight_layout()
        filename = join(self.params["path graphics"],
                        self.params["file map"])
        plt.savefig(filename,
                    dpi=500)
