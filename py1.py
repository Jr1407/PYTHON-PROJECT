Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
... import numpy as np
... 
... batchName = np.array([0, 1, 2, 3])
... averagePercentage = np.array([3, 8, 1, 10])
... 
... plt.xlabel("Batch Name")
... plt.ylabel("Average Percentage")
... plt.title('Line Plot')
... 
... plt.plot(batchName,averagePercentage, c = '#4CAF50', linewidth = '8')
