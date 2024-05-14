"""

1. Prints  "symbolic maths notation" to the screen to the screen, in this example an Integration formula
2. Uses HTML code to print to the screen through a web browser
3. Uses a LaTex type formula to represent the symbolic maths notation. This formula is also printed in he output consul
    and can be cut and copied as needed, for example to an MS MS Word equation
4.Includes example of parameters to alter size, font , placement etc of both the mathematical formula and the descriptive header
54. Includes code to solve the mathematical equation provided






"""

import sympy as sp
from weasyprint import HTML

# Define symbols and expressions
x = sp.symbols('x')
expression = sp.sin(x**2) + sp.cos(x)

# Create unevaluated Integral object
integral_expr = sp.Integral(expression, (x, 0, sp.pi))

# Convert integral result into customized LaTeX string with larger integral sign and bounds.
latex_integral_expression = r"\displaystyle\int_{" + str(sp.latex(0)) \
                            + "}^{"+ str(sp.latex(sp.pi)) + "}" \
                            r"\! \normalsize(" + str(sp.latex(expression)) \
                            + r") \mathrm{d}" + str(sp.latex(x))

# Prepare the HTML content with embedded MathJax for LaTeX rendering.
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Integral Display</title>
    <!-- Load MathJax -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body style='font-size:20px; text-align:center;'>
<h1>Displaying Calculus Integration:</h1>

<!-- Embedding Latex Code Directly with class for styling -->
<div style='font-size:24px;'>\\({latex_integral_expression}\\)</div>

</body>
</html>
"""

# Write html content into an html file (optional - useful for debugging)
with open("integral_output.html", "w") as file:
    file.write(html_content)

# Use WeasyPrint to render the HTML directly into a PDF.
HTML(string=html_content).write_pdf("output.pdf")

print("PDF has been created.")

