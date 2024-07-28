import numpy as np

# Construct the data
x = np.array([0,  1,  2,  3,  4,  5, 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
y = np.array([667070000, 660330000, 665770000, 682335000, 698355000, 715185000, 735400000, 754550000, 774510000, 796025000, 818315000, 841105000, 862030000, 881940000, 900350000, 916395000, 930685000, 943455000, 956165000, 969005000, 981235000, 993885000, 1008630000, 1023310000, 1036825000, 1051040000, 1066790000, 1084035000, 1101630000, 1118650000, 1135185000, 1150780000, 1164970000, 1178440000, 1191835000, 1204855000, 1217550000, 1230075000, 1241935000, 1252735000, 1262645000, 1271850000])

#, 1280400000, 1288400000, 1296075000, 1303720000, 1311020000, 1317885000, 1324655000, 1331260000, 1337705000

# Construct the matrix [x]
ones = np.ones(len(x))
X = np.vstack([x**2, x, ones]).T

# Solve the least squares equation
a, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

# Print the result
print(a)

import matplotlib.pyplot as plt

# Plot the data points
plt.plot(x, y, 'o', label='Data')

# Compute the approximated function
x_values = np.linspace(x[0], x[-1], 100)
y_values = a[0] * x_values**2 + a[1] * x_values + a[2]

# Plot the approximated function
plt.plot(x_values, y_values, '-', label='Least-squares fit')

# Add a legend and show the plot
plt.legend()
plt.xlabel('Time / yrs')
plt.ylabel('Population in hundreds of millions')
plt.title('Quadratic Model')

plt.show()

