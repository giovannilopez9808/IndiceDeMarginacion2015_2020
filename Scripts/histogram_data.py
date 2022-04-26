from Modules.params import get_params, get_classes_colors
from matplotlib.container import BarContainer
from Modules.data_model import data_class
import matplotlib.pyplot as plt
from os.path import join


def autolabel(bars: BarContainer) -> None:
    for bar in bars:
        height = bar.get_height()
        pos = (bar.get_x()+bar.get_width()/2, height)
        plt.annotate('{:.1f}%'.format(height),
                     xy=pos,
                     # 3 points vertical offset
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center',
                     va='bottom')


years = [2015, 2020]
for year in years:
    print("-"*30)
    print("Analizando año {}".format(year))
    params = get_params(year)
    params["file graphics"] = "histogram_classes.png"
    colors = get_classes_colors(params)
    data = data_class(params)
    frecuency = data.obtain_frecuency_clasees()
    frecuency = 100*frecuency/frecuency.sum()
    plt.subplots(figsize=(10, 4))
    bars = plt.bar(frecuency.index,
                   frecuency.values,
                   color=colors.values())
    autolabel(bars)
    plt.xlabel("Grado de marginación")
    plt.ylabel("Porcentaje de municipios")
    plt.ylim(0, 30)
    plt.grid(ls="--",
             alpha=0.5,
             color="#000000",
             axis="y")
    plt.tight_layout()
    filename = join(params["path graphics"],
                    params["file graphics"])
    plt.savefig(filename,
                dpi=300)
