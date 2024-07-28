import matplotlib.pyplot as plt
import numpy as np

# define the data points
x = np.array([42, 43, 44, 45, 46, 47,
              48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
y = np.array(
    [1280400000, 1288400000, 1296075000, 1303720000, 1311020000, 1317885000, 1324655000, 1331260000, 1337705000,
     1345035000, 1354190000, 1363240000, 1371860000, 1379860000, 1387790000, 1396215000, 1402760000, 1407745000,
     1411100000, 1412360000])
z = np.array([1283018263, 1293397697, 1303489550, 1313296277, 1322820730, 1332066129, 1341036029, 1349734295, 1358165066, 1366332732,
1374241907, 1381897398, 1389304183, 1396467385, 1403392253, 1410084135, 1416548460, 1422790717, 1428816441, 1434631190])

# plot the data points and the function
plt.scatter(x, y, label='Actual population')
plt.scatter(x, z, label='Estimated population')


# add a legend and show the plot
plt.legend()
#plt.scatter(x, z)
plt.xlabel('Time / yrs')
plt.ylabel('Population in hundreds of millions')
plt.title('Comparison with Logistic Model')
plt.show()
