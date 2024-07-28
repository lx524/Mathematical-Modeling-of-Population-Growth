import matplotlib.pyplot as plt
import numpy as np

# define the data points
x = np.array([42, 43, 44, 45, 46, 47,
              48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
y = np.array(
    [1280400000, 1288400000, 1296075000, 1303720000, 1311020000, 1317885000, 1324655000, 1331260000, 1337705000,
     1345035000, 1354190000, 1363240000, 1371860000, 1379860000, 1387790000, 1396215000, 1402760000, 1407745000,
     1411100000, 1412360000])
z = np.array([1290036709, 1302062817, 1313924011, 1325620293, 1337151661, 1348518117, 1359719659, 1370756289, 1381628006, 1392334810, 1402876701, 1413253679, 1423465744, 1433512896, 1443395135, 1453112462, 1462664875, 1472052376, 1481274963, 1490332638])

# plot the data points and the function
plt.scatter(x, y, label='Actual population')
plt.scatter(x, z, label='Estimated population')


# add a legend and show the plot
plt.legend()
#plt.scatter(x, z)
plt.xlabel('Time / yrs')
plt.ylabel('Population in hundreds of millions')
plt.title('Comparison with Quadratic Model')
plt.show()
