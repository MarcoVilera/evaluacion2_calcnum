from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
import numpy as np
x,y,z = symbols('x y z')

eq1 = Eq((5*x + 3*y + 2*z),20)
eq2 = Eq((4*x+6*y-5*z),-2)
eq3 = Eq((5*x+y-z),21)

solution = solve([eq1,eq2,eq3],(x,y,z))
print("Equation 1: ", eq1)
print("Equation 2: ", eq2)
print("Equation 3: ", eq3)
print("Solution: ", solution)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a range of values for x and y
x_range = np.linspace(-10, 10, 10)
y_range = np.linspace(-10, 10, 10)

# Create a grid of x and y values
x_grid, y_grid = np.meshgrid(x_range, y_range)

# Calculate corresponding z values for the grid
z_grid1 = (20 - 5*x_grid - 3*y_grid) / 2
z_grid2 = (2 + 4*x_grid + 6*y_grid) / 5
z_grid3 = 21 - 5*x_grid - y_grid

# Plot the surfaces
ax.plot_wireframe(x_grid, y_grid, z_grid1, color='blue', label='5x + 3y + 2z = 20')
ax.plot_wireframe(x_grid, y_grid, z_grid2, color='green', label='4x + 6y - 5z = -2')
ax.plot_wireframe(x_grid, y_grid, z_grid3, color='orange', label='5x + y - z = 21')

# Plot the solution
ax.scatter([solution[x]], [solution[y]], [solution[z]], color='red', label='Solution')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
