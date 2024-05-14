"""

1. Prints  "symbolic maths notation" to the screen to the screen, in this example an Integration formula
2. Uses HTML code to print to the screen through a web browser
3. Uses a LaTex type formula to represent the symbolic maths notation. This formula is also printed in he output consul
    and can be cut and copied as needed, for example to an MS MS Word equation
4.Includes example of parameters to alter size, font , placement etc of both the mathematical formula and the descriptive header
54. Includes code to solve the mathematical equation provided






"""

### Method 1: Using Matplotlib

import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.pyplot as plt
import sympy as sp

# Define symbols and expression
x = sp.symbols('x')
expression = sp.sin(x ** 2) + sp.cos(x)

try:
  # Attempt to integrate the expression
  integral_expr = sp.Integral(expression, (x, 0, sp.pi))
except (NotImplementedError, ValueError) as e:
  print(f"Error during integration: {e}")
  exit(1)  # Exit with an error code




# Define symbols and expression
x = sp.symbols('x')
expression = sp.sin(x ** 2) + sp.cos(x)
integral_expr = sp.Integral(expression, (x, 0, sp.pi))

# Convert integral result into LaTeX string
latex_integral_expression = r"$\displaystyle" + sp.latex(integral_expr) + "$"

# Plotting setup (to use Latex style)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Create figure and axis objects
fig, ax = plt.subplots()

# Add text to the plot - centered on the canvas.
ax.text(0.5, 0.5, latex_integral_expression,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=15,
        transform=ax.transAxes)

# Remove axes as they are unnecessary here.
ax.axis('off')

# Save the plot to a PDF file.
fig.savefig("output.pdf")

print("PDF has been created.")


