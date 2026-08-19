import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')
#  https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    
votes = [10,2,5,16,22]

people= ["A","B","C","D","E"]

plt.pie(votes,labels=None)
plt.legend(labels=people)
plt.show()

plt.show()