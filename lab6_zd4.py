import numpy as np
A = np.arange(6).reshape(2, 3)
B = np.arange(6).reshape(3, 2)
print(A)
print(B)

skala = np.dot(A, B)
skalb = np.dot(B, A)
B = np.reshape(3, 3)
print("skalarny a-b:", skala)
print("skalarny b-a: ", skalb)