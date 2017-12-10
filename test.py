# a new random file
import random
a = [random.randint(10,30) for i in range(15)]
b = [random.gauss(0,1) for i in range(15)]

import matplotlib.pyplot as plt
plt.plot(x=a, y=b)
plot.show()