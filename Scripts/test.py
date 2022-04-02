from Modules.data_model import data_class
from Modules.params import get_params
from Modules.models import PCA_model
import matplotlib.pyplot as plt
from numpy import array

params = get_params()
data = data_class(params)
pca = PCA_model()
pca.create(3)
pca.run(data.embedding)
results = pca.model.components_.T
for classes in data.classes:
    index = array(data.data_2020.index[data.data_2020["GM"] == classes])
    color = data.classes[classes]["color"]
    subset = results[index]
    plt.scatter(subset[:, 0],
                subset[:, 1],
                alpha=0.3,
                c=color,
                label=classes)
plt.tight_layout()
plt.axis("off")
plt.show()
