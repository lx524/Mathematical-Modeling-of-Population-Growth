import matplotlib.pyplot as plt

# Define the function representing the right hand side of the differential equation
def logistic_model(x, t, r, K):
    return r * x * (1 - x/K)

# Set the carrying capacity
K = 100

# Set the time step
dt = 0.01

# Initialize lists to store the solutions
t_values = []
x_values_1 = []
x_values_2 = []
x_values_3 = []

# Approximate the solutions using the Euler method
t = 0
x1 = 5
x2 = 10
x3 = 120
while t <= 20:
    x_values_1.append(x1)
    x_values_2.append(x2)
    x_values_3.append(x3)
    t_values.append(t)
    x1 = x1 + dt * logistic_model(x1, t, 0.3, K)
    x2 = x2 + dt * logistic_model(x2, t, 0.5, K)
    x3 = x3 + dt * logistic_model(x3, t, 0.9, K)
    t = t + dt


fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
ax.set_yticks([0, 50, 100])
ax.set_yticklabels([0, 'M/2', 'M'])

# Plot the solutions
plt.plot(t_values, x_values_1)
plt.plot(t_values, x_values_2)
plt.plot(t_values, x_values_3)

# line colour is black
plt.axhline(y = 100, color = 'black', linestyle = 'dashed')
plt.axhline(y = 50, color = 'black', linestyle = 'dotted')

plt.xticks(color='w')

# Add labels and title
plt.xlabel('t / yrs')
plt.ylabel('P')
plt.legend()

# Show the plot
plt.show()
