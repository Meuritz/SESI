import numpy as np
import matplotlib.pyplot as plt

# We generate a list with 100 numbers
x = np.linspace(0, 2 * np.pi, 100)

# Two variables for storing the output of the 2 trigonometric functions
x_cos = np.cos(x)
x_sin = np.sin(x)

# Settings for the plot

# What we want to plot and its properties
plt.plot(x_cos)
plt.plot(x_sin)

# Print the plot to the screen
plt.show()