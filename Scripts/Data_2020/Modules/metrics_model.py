from sklearn.metrics import calinski_harabasz_score, fowlkes_mallows_score, confusion_matrix
import matplotlib.pyplot as plt
from numpy import array, arange
from os.path import join


class metrics_class:
    def __init__(self, params: dict, data: array) -> None:
        self.params = params
        self.data = data

    def apply_all_metrics(self, true_label: array, model_label: array) -> dict:
        results = {}
        results["Calinski Harabasz model"] = self.get_CH_score(self.data,
                                                               model_label)
        results["Calinski Harabasz true"] = self.get_CH_score(self.data,
                                                              true_label)
        results["Fowlkes Mallows"] = self.get_FM_score(true_label,
                                                       model_label)
        matrix = self.get_confusion_matrix(true_label,
                                           model_label)
        self.plot_confusion_matrix(matrix)
        return results

    def get_CH_score(self, data: array, model_label: array) -> float:
        ch_scores = calinski_harabasz_score(data, model_label)
        return ch_scores

    def get_FM_score(self, true_label: array, model_label: array) -> float:
        score = fowlkes_mallows_score(true_label,
                                      model_label)
        return score

    def get_confusion_matrix(self, true_label: array, model_label: array) -> array:
        matrix = confusion_matrix(true_label,
                                  model_label)
        return matrix

    def plot_confusion_matrix(self, matrix: array) -> None:
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
