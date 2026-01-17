import numpy as np
A = np.arange(25).reshape(5, 5)
print(A)

gora = A[0, :]
dol = A[-1, :]
lewo =A[:, 0]
prawo = A[:, -1]

print("1 wiersz: ", gora)
print("5 wiersz: ", dol)
print("1 kolumna: ", lewo)
print("5 kolumna: ", prawo)