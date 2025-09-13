import numpy as np

array = np.array(
    [
        [
            [3, 2, 1],
            [4, 5, 6]
        ],
        [
            [9, 2, 31],
            [4, 15, -6]
        ]
    ]
)
print(array[1, 0, 2])
print(array.shape)
print(array.ndim)
print(array.size)
print(array.dtype)
print(array)