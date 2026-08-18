import numpy as np
import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]
weights = [80,83,84,86,87,79,80,81,82,82,80,78,79,81,82,80]
plt.plot(years, weights, "r--", lw = 3)
plt.show()