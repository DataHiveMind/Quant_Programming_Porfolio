import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(torch.__version__)

scalar = torch.tensor(7)
print(scalar,
      scalar.ndim)

scalar.item()
vector = torch.tensor([7,7])
print(vector, vector.ndim)
print(vector.shape)

matrix = torch.tensor([[7, 8,], 
                      [9, 10]])
print(matrix, matrix.ndim)
print(matrix[1])
print(matrix.shape)

ten = torch.tensor([[[1, 2, 3], 
                     [3, 6, 9],
                     [2, 4, 5]]])
print(ten)
print(ten.ndim)
print(ten.shape)
print(ten[0])

random_tensor = torch.rand(10, 10, 10)
print(random_tensor)
print(random_tensor.ndim)

rand_size = torch.rand(224, 224, 3)
print(rand_size.shape, rand_size.ndim)

zero = torch.zeros(size = (3,4))
print(zero, zero*random_tensor)

ones = torch.ones(size = (3, 4))
print(ones.dtype, random_tensor.dtype)

one = torch.arange(start = 1, end = 1000, step = 77)
print(one)
