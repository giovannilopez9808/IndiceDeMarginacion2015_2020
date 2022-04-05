from geopandas import read_file, GeoDataFrame
from .data_model import data_class, join
from .params import get_classes_colors
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt


class map_model:
    def __init__(self, params: dict) -> None:
        self.params = params
        self.read()

    def read(self) -> GeoDataFrame:
        self.data = read_file(self.params["path map"])
        self.data = self.data.rename(columns={"CLAVE": "CVE_MUN"})

    def merge(self, data: data_class) -> GeoDataFrame:
        self.data = self.data.merge(data.data_2020, on="CVE_MUN")

    def plot_GM(self) -> None:
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
                               frameon=False,
                               ncol=5,
                               loc=(0.3, 0.96))
        ax.add_artist(leg_points)
        ax.axis("off")
        plt.tight_layout()
        filename = join(self.params["path graphics"],
                        self.params["file map"])
        plt.savefig(filename)
