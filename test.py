import numpy as np 
import torch 

np.random.seed(123)
tensor = torch.tensor(np.random.randint(0, 10, size = 5), dtype = torch.float32)

print(tensor)