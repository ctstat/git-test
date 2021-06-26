import numpy as np 
import matplotlib.pyplot as plt   

np.random.seed(12)

x = list(range(11))

a, b = 0.5, np.pi
y = np.cos([(a + b*i) for i in x])

plt.scatter(x, y, marker= "+")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()