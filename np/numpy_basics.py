import numpy as np

array = np.arange(1, 6)
print(array)

print(array[0])
print(array[4], array[-1])

print(array[1:4], array[1:-1])
print(array[::2])

arr2d = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
)
print(arr2d[0, 1])
print(arr2d[:, 1])