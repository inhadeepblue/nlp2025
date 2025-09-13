import numpy as np

# np.random.seed(50)

x = np.random.random(5)
print(x)
y = np.random.randint(1, 7, 5)
print(y)
z = np.random.normal(50, 10, 5)
print(z)
# q = np.arange(1, 6)
# choice = np.random.choice(q, 3)
# print(choice)

q = np.array(["가위", "바위", "보"])
choice = np.random.choice(q, 2)
print(choice)