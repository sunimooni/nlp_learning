import numpy as np

a = np.arange(10)
b = np.arange(1,10,2)
c = np.arange(30)
print(type(c))
c = np.array(c)
print(type(c))
d = c.reshape((5,6))

print(d)
print(c)
print(b)
print(a)



