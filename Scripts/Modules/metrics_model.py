from sklearn.metrics import calinski_harabasz_score, fowlkes_mallows_score, confusion_matrix
import matplotlib.pyplot as plt
from numpy import array, arange
from os.path import join


class metrics_class:
    """
    Modelo que aplica las metricas siguientes 
    + Calinski Harabasz
    + Fowlkes Mallows
    + Confusion matrix

    Se guarda un archivo y la gráfica de la confusion matrix con el nombre del metodo con todas sus metricas
    """

    def __init__(self, params: dict, data: array) -> None:
        self.params = params
        self.data = data

    def apply_all_metrics(self, true_label: array, model_label: array) -> dict:
        results = {}
        results["Calinski Harabasz model"] = self._get_CH_score(self.data,
                                                                model_label)
        results["Calinski Harabasz true"] = self._get_CH_score(self.data,
                                                               true_label)
        results["Fowlkes Mallows"] = self._get_FM_score(true_label,
                                                        model_label)
        self._get_confusion_matrix(true_label,
                                   model_label)
        return results

    def _get_CH_score(self, data: array, model_label: array) -> float:
        """
        Obtiene el Calinski Harabasz score a las etiquetas dadas
        """
        ch_scores = calinski_harabasz_score(data, model_label)
        return ch_scores

    def _get_FM_score(self, true_label: array, model_label: array) -> float:
        """
        Obtiene el Fowlkes Mallows score a las etiquetas dadas
        """
        score = fowlkes_mallows_score(true_label,
                                      model_label)
        return score

    def _get_confusion_matrix(self, true_label: array, model_label: array) -> None:
        """
        Obtiene la confision matrix de las etiquetas dadas
        """
        matrix = confusion_matrix(true_label,
                                  model_label)
        self._plot_confusion_matrix(matrix)
        return matrix

    def _plot_confusion_matrix(self, matrix: array) -> None:
        """
        Grafica la confusion matrix obtenida
        """
        fig, ax = plt.subplots()
        ax.imshow(matrix)
        class_labels = list(self.params["classes"].keys())
        len_class_labels = len(class_labels)
        ax.set_xticks(arange(len_class_labels),
                      labels=class_labels)
        ax.set_yticks(arange(len_class_labels),
                      labels=class_labels)
        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(),
                 rotation=45,
                 ha="right",
                 rotation_mode="anchor")
        # Loop over data dimensions and create text annotations.
        for i in range(len_class_labels):
            for j in range(len_class_labels):
                ax.text(j, i, matrix[i, j],
                        ha="center",
                        va="center",
                        color="w")
        ax.set_xlabel("Etiquetas correctas")
        ax.set_ylabel("Predicción de etiquetas")
        ax.set_title(self.params["model name"])
        fig.tight_layout()
        filename = join(self.params["path graphics"],
                        self.params["file graphics"])
        plt.savefig(filename, dpi=300)
