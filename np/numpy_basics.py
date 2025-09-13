import numpy as np

m = np.array([4, 25, 9, 16])
print(np.sqrt(m))
print(np.exp(m))
print(np.log(m))
n = np.array([0, np.pi/2, np.pi])
print(n)
print(np.sin(n))
print(np.cos(n))

r = m.reshape(2, 2)
print(r)
# t = r.transpose()
t = r.T
print(t)