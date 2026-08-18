import numpy as np
import matplotlib.pyplot as plt

X_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

plt.scatter(X_data, y_data, color='blue', marker='o')
plt.show()