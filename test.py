# a new random file
import random
a = [random.randint(10,30) for i in range(15)]
b = [random.gauss(0,1) for i in range(15)]

# print c
c = [i*j for i, j in zip(a, b)]
print(c)