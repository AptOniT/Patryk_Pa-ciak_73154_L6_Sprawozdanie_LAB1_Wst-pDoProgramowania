import numpy as np
rng = np.random.default_rng(42)
a = rng.normal(0, 1, size= (6, 4))
print(a)
x = a.mean(axis=0)
e = a.max(axis=0)
f = a.min(axis=0)

print("średnia kolumn: ", x)
print("maksymalny indeks: ", e)
print("minimalny indeks: ", f)


