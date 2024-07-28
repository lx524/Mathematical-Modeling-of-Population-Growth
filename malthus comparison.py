import matplotlib.pyplot as plt
import numpy as np

# define the data points
x = np.array([42, 43, 44, 45, 46, 47,
              48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
y = np.array(
    [1280400000, 1288400000, 1296075000, 1303720000, 1311020000, 1317885000, 1324655000, 1331260000, 1337705000,
     1345035000, 1354190000, 1363240000, 1371860000, 1379860000, 1387790000, 1396215000, 1402760000, 1407745000,
     1411100000, 1412360000])
z = np.array([1371262748, 1394992430, 1419132755, 1443690827, 1468673877, 1494089258,
              1519944451, 1546247069, 1573004853, 1600225679, 1627917562, 1656088653, 1684747244, 1713901771,
              1743560818, 1773733113, 1804427540, 1835653133, 1867419085, 1899734746])

# plot the data points and the function
plt.scatter(x, y, label='Actual population')
plt.scatter(x, z, label='Estimated population')


# add a legend and show the plot
plt.legend()
#plt.scatter(x, z)
plt.xlabel('Time / yrs')
plt.ylabel('Population in hundreds of millions')
plt.title('Comparison with Malthus Model')
plt.show()
