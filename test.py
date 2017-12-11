# a new random file
import random
a = [random.randint(10,30) for i in range(15)]
b = [random.gauss(0,1) for i in range(15)]
c = [i * j for i, j in zip(a, b)]


import matplotlib.pyplot as plt
plt.scatter(x=a, y=b)
plt.show()

