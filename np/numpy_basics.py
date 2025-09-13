import numpy as np

a = np.arange(1, 6)

mask = a > 2
print(a[mask])

# result = np.where(a > 3, a, a**2)
result = np.where(a > 3, a, 0)
print(result)