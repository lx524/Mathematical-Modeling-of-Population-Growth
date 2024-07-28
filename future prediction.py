import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
              24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
y = np.array(
[667070000, 660330000, 665770000, 682335000, 698355000, 715185000, 735400000, 754550000, 774510000, 796025000,
     818315000, 841105000, 862030000, 881940000, 900350000, 916395000, 930685000, 943455000, 956165000, 969005000,
     981235000, 993885000, 1008630000, 1023310000, 1036825000, 1051040000, 1066790000, 1084035000, 1101630000,
     1118650000, 1135185000, 1150780000, 1164970000, 1178440000, 1191835000, 1204855000, 1217550000, 1230075000,
     1241935000, 1252735000, 1262645000, 1271850000, 1280400000, 1288400000, 1296075000, 1303720000, 1311020000, 1317885000, 1324655000, 1331260000, 1337705000, 1345035000, 1354190000, 1363240000, 1371860000, 1379860000, 1387790000, 1396215000, 1402760000, 1407745000, 1411100000, 1412360000])

# Define the model function
def model(x, M, A, k):
    return M / (1 + A * np.exp(-k * x))

# Use curve_fit to find the optimal parameters
params, params_covariance = curve_fit(model, x, y)

# The optimal parameters are stored in the params variable
M, A, k = params

# Define a range of x values to use for plotting the approximation line
x_range = np.linspace(min(x), max(x), 100)

# Calculate the corresponding y values for the approximation line
y_approx = model(x_range, M, A, k)

# Plot the data points and the approximation line
plt.plot(x, y, 'bo', label='Data')
plt.plot(x_range, y_approx, 'r', label='Best-fit curve')

# Add a legend and axis labels
plt.legend()
plt.xlabel('Time / yrs')
plt.ylabel('Population in hundreds of millions')
plt.title('Logistic Model')

# Show the plot
plt.show()

print("M = ", M)
print("A = ", A)
print("k = ", k)