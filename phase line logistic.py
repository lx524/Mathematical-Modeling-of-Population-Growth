import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x)
def f(x):
    return (1.8 * x * (5 - x)) / 5

# Generate x values to plot with a finer resolution
x = np.linspace(0, 6, 100)

# Calculate y values for each x value
y = (1.8 * x * (5 - x)) / 5

# Plot the function
#plt.plot(x, y)



#plt.xticks(color='w')
#plt.yticks(color='w')

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
ax.plot(x, y)
ax.set_xticks([0, 2.5, 5])
ax.set_xticklabels([0, 'M/2', 'M'])
ax.set_yticks([0])

plt.plot([2.5], [2.25], 'ro')

# Add labels and title
plt.xlabel('P')
plt.ylabel('dP/dt')

# line colour is red
plt.axhline(y = 0, color = 'r', linestyle = 'dashed')

# Show the plot
plt.show()
