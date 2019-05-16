import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([[1,2,3],[4,5,6]])
print(type(b))
print(b)
print(b.ndim)
print(b.shape)
print(type(a))
print(a)
print('\n\n')

a = np.zeros((2,3))
b = np.ones((2,3))
c = np.full((2,2), 7)
d = np.eye(3)
e = np.random.random((2,3))

print(e)
print(d)
print(c)
print(b)
print(a)



