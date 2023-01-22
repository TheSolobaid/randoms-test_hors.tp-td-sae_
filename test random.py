import numpy as np
b = []
a = np.array([3,4,2,7,32])

print(a)
print(type(a))

b.append(a)
print(b)
print(type(b))

c = a.tolist()
print(c)
print(type(c))