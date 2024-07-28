import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# define the data points as a list of tuples
x = np.array([0,  1,  2,  3,  4,  5, 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
y = np.array([667070000, 660330000, 665770000, 682335000, 698355000, 715185000, 735400000, 754550000, 774510000, 796025000, 818315000, 841105000, 862030000, 881940000, 900350000, 916395000, 930685000, 943455000, 956165000, 969005000, 981235000, 993885000, 1008630000, 1023310000, 1036825000, 1051040000, 1066790000, 1084035000, 1101630000, 1118650000, 1135185000, 1150780000, 1164970000, 1178440000, 1191835000, 1204855000, 1217550000, 1230075000, 1241935000, 1252735000, 1262645000, 1271850000])


# define the function to fit
def func(x, a, k):
    return a * np.exp(k * x)

# fit the curve to the data
params, cov = curve_fit(func, x, y)

# extract the fit parameters
a, k = params

# print the fit parameters
print(f'a = {a:.2f}, k = {k:.2f}')

# generate a set of x values for the curve
x_curve = np.linspace(min(x), max(x), 100)

# compute the y values for the curve
y_curve = func(x_curve, a, k)

# plot the curve
plt.plot(x, y, 'bo', label='Data')
plt.plot(x_curve, y_curve, 'r', label='Best-fit curve')

# add a legend and show the plot
plt.legend()
plt.xlabel('Time / yrs')
plt.ylabel('Population in hundreds of millions')
plt.title('Malthus Model')
plt.show()
