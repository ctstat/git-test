import numpy as np  

X = np.array([[1, 1.015, 6.79],
              [1, 1.01, 5.97],
              [1, 1.02, 5.68],
              [1, 1.021, 5.94],
              [1, 1.024, 5.77],
              [1, 1.024, 5.6]])

y = np.array([[0], [0], [0], 
              [1], [1], [1]])



def loss(b, w1, w2):
    return -1*sum(y*np.log(1/(1+np.exp(-(b*x[0] + w1*x[1] + w2*x[2])))) + 
                 (1-y)*np.log(1 - 1/(1+np.exp(-(b*x[0] + w1*x[1] + w2*x[2])))) for x, y in zip(X, y))

def d_loss_b(b, w1, w2):
    return -1*sum(np.exp(-(b*x[0] + w1*x[1] + w2*x[2]))/(1+ np.exp(-(b*x[0] + w1*x[1] + w2*x[2])))**2 for x, y in zip(X, y))                                

def d_loss_w1(b, w1, w2):
    return -1*sum(x[1]*np.exp(-(b*x[0] + w1*x[1] + w2*x[2]))/(1+ np.exp(-(b*x[0] + w1*x[1] + w2*x[2])))**2 for x, y in zip(X, y))                                


def d_loss_w2(b, w1, w2):
    return -1*sum(x[2]*np.exp(-(b*x[0] + w1*x[1] + w2*x[2]))/(1+ np.exp(-(b*x[0] + w1*x[1] + w2*x[2])))**2 for x, y in zip(X, y))                                


eta = 0.01
b, w1, w2 = (0, 0.5, 0.5)

for i in range(3000):
    Loss = loss(b, w1, w2)
    gradient_b = d_loss_b(b, w1, w2)
    gradient_w1 = d_loss_w1(b, w1, w2)
    gradient_w2 = d_loss_w2(b, w1, w2)
    b = b - eta*gradient_b
    w1 = w1 - eta*gradient_w1
    w2 = w2 - eta*gradient_w2
    print(f"iteration:{i+1}, Loss = {Loss}, b = {b}, w1 = {w1}, w2 = {w2}")
