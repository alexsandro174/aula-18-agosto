import numpy as np

# Exercício 1
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C1 = np.dot(A, B)
print("Exercício 1 - A x B =\n", C1, "\n")

# Exercício 2
M = np.array([[2, -1, 3],
              [0, 4, 5]])

N = np.array([[1, 2],
              [-2, 0],
              [3, 1]])

C2 = np.dot(M, N)
print("Exercício 2 - M x N =\n", C2, "\n")

# Exercício 3
X = np.array([[1, 0, 2],
              [-1, 3, 1],
              [4, -2, 5]])

Y = np.array([[2, -3, 1],
              [0, 4, -2],
              [-1, 5, 3]])

C3 = np.dot(X, Y)
print("Exercício 3 - X x Y =\n", C3)
