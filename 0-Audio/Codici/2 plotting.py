import numpy as np
import matplotlib.pyplot as plt

# We generate a list with 100 numbers
x = np.linspace(0, 2 * np.pi, 100)

# Two variables for storing the output of the 2 trigonometric functions
x_cos = np.cos(x)
x_sin = np.sin(x)

# Settings for the plot
plt.title("Funzioni seno e coseno")
plt.xlabel("Ascisse")
plt.ylabel("Ordinate")

# What we want to plot and its properties
plt.plot(x_cos, "purple", label="Coseno", linestyle="dotted")
plt.plot(x_sin, "green", label="Seno", linestyle="dashed")

#to show the x and y axis
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

# To show the legend
plt.legend()

# Print the plot to the screen
plt.show()