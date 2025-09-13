import numpy as np

o = np.arange(1, 13)

# r = o.reshape(2, 2, 3)
r = o.reshape(4, 3)
print(o)
print(r)
f = r.flatten()
print(f)