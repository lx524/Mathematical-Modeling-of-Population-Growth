import numpy as np

# Construct the data
x = np.array([19, 25, 31, 38, 44])
y = np.array([19, 32.3, 49, 73.3, 97.8])

# Construct the matrix [x]
ones = np.ones(len(x))
X = np.vstack([x**2, x, ones]).T

# Solve the least squares equation
a, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

# Print the result
print(a)
