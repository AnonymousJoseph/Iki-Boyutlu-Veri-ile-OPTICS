from sklearn.cluster import OPTICS
import numpy as np

# İki boyutlu verinin oluşturulması
X = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [7, 8, 9], [8, 9, 10], [9, 10, 11]])

# OPTICS modelinin oluşturulması
clustering = OPTICS(min_samples=2).fit(X)

# Kümelerin çıktısını almak
print(clustering.labels_)
