import numpy as np
import matplotlib.pyplot as plt

gamma = 1.4

M = np.linspace(0.1,5,500)

A_ratio = (1/M)*((2/(gamma+1))*(1+((gamma-1)/2)*M**2))**((gamma+1)/(2*(gamma-1)))

plt.plot(M,A_ratio)

plt.xlabel("Mach Number")
plt.ylabel("Area Ratio")
plt.title("Area Ratio vs Mach Number")

plt.grid(True)
plt.show()
