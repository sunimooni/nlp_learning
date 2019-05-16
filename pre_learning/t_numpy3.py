import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = a[0:2, 0:2]
c = np.array([[1,2],[3,4],[5,6]])
d = c[[2,1],[1,0]]

print(c)
print(d)
