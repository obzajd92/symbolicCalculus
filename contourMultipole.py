pythonimport numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ==========================================
# 1. Symbolic Symbolic Formulation & Calculus
# ==========================================
z = sp.symbols('z')

# Define the analytic numerator function f(z) and the pole z0
f_z = sp.exp(z)
z0 = 0.5

# Full integrand expression for the characteristic function
integrand = f_z / (z - z0)

print("--- Characteristic Function ---")
print(f"Before Integration: g(z) = {integrand}")

# Apply Cauchy's Integral Formula: \oint f(z)/(z - z0) dz = 2 * pi * i * f(z0)
integral_value = 2 * sp.I * sp.pi * f_z.subs(z, z0)
print(f"After Integration:  I    = {sp.simplify(integral_value)}\n")

# Compute the Residue analytically at z = z0
residue = sp.residue(integrand, z, z0)
print(f"Calculated Residue at z = {z0}: {residue}\n")


# ==========================================
# 2. Geometric Complex Plane Visualization
# ==========================================
# Define the circular contour boundary (Unit Circle |z| = 1)
theta = np.linspace(0, 2 * np.pi, 400)
contour_x = np.cos(theta)
contour_y = np.sin(theta)

fig, ax = plt.subplots(figsize=(7, 7))

# Area of integration filled in Light Blue
ax.fill(contour_x, contour_y, color='lightblue', alpha=0.5, label='Area of Integration')

# Contour limits/bounds highlighted in Light Red
ax.plot(contour_x, contour_y, color='lightcoral', linewidth=3, label='Integral Bounds ($|z|=1$)')

# Plot the pole location
ax.scatter([float(z0)], [0.0], color='red', s=100, zorder=5, 
           label=f'Interior Pole ($z_0 = {z0}$)\nResidue = {float(residue):.4f}')

# Grid alignment and axes aesthetic
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Real Axis ($\mathcal{Re}$)')
ax.set_ylabel('Imaginary Axis ($\mathcal{Im}$)')
ax.set_title('Cauchy Integral Visualization & Residue Plot', fontsize=12, fontweight='bold')
ax.set_aspect('equal', 'box')
ax.grid(True, which='both', alpha=0.3)
ax.legend(loc='upper right')

# Show the plot
plt.show()
Use code with caution.Visual and Mathematical BehaviorThe code maps the integral domain onto a standard complex coordinate mesh grid:Characteristic Function: Expresses the singular map \(g(z)\) capturing geometric weights before collapsing to a scalar boundary map (\(2\pi i \cdot e^{0.5}\)) upon integration.Area of Integration: Colored cleanly in light blue, representing the interior open domain bounded by \(\vert{}z\vert{} \leq 1\).Integral Bounds: Outlined in light red, visualizing the explicit contour limits where the integration paths line up.Would you like to extend this script to handle multiple poles simultaneously, or modify the contour path from a circle to a polygonal rectangle?YouTube·tondekushHow to do contour integration with Python & SymPy using the residue ...uh hey guys uh hope you're well yeah so today we're going to look at uh um integrating on the complex plane. okay um just following through what I've done with9:59Reddit·Mr. P SolverHow to Solve Integrals in Python: A Complete and Quick Guide to ...In this video I show how to solves symbolically and numerically using sympy and scipy. In particular, for a given integral, I give a sequence of steps. Firstly,15:20extend this script to handle multiple poles
then print characteristic function before after integration with its residue . draw the characteristics function with the area of integration as previously specifiedHere is the extended script that dynamically identifies all poles inside a given boundary, computes the total contour integral using the Residue Theorem (which generalizes Cauchy's Integral Formula), and plots both the integration region and the geometric structure of the characteristic function.Python Script for Multiple Polespythonimport numpy as np
import matplotlib.pyplot as plt
import sympy as sp


"""
script accepts an arbitrary array of complex points (poles), factors the denominator automatically, and checks whether each coordinate sits inside the unit vector radius before inclusion.
"""
# ==========================================
# 1. Mathematical Definition & Symbolic Computation
# ==========================================
z = sp.symbols('z')

# Define a numerator function f(z) that is analytic inside the contour
f_z = sp.exp(z)

# Define the poles to place inside the unit circle
poles = [0.4 + 0.3j, -0.5 - 0.2j] 

# Construct the denominator dynamically based on the poles
denominator = 1
for p in poles:
    denominator *= (z - p)

# Define the characteristic function (integrand)
integrand = f_z / denominator

print("--- Characteristic Function (Integrand) ---")
print(f"g(z) = {sp.simplify(integrand)}\n")

# Calculate residues and determine which poles lie inside the unit circle (|z| < 1)
total_integral = 0
valid_poles = []
residues = []

print("--- Pole Analysis & Residues ---")
for p in poles:
    # Check if the pole lies inside the unit circle boundary
    if np.abs(p) < 1.0:
        res_val = sp.residue(integrand, z, p)
        valid_poles.append(p)
        residues.append(res_val)
        total_integral += res_val
        print(f"Pole at z = {p:<15} -> Residue = {sp.N(res_val, 4)}")

# Apply the Residue Theorem: \oint g(z) dz = 2 * pi * i * \sum(Residues)
integral_result = 2 * sp.I * sp.pi * total_integral

print("\n--- Integration Result ---")
print(f"Value After Integration: I = {sp.simplify(integral_result)}")
print(f"Numerical Approximation: I ≈ {sp.N(integral_result, 4)}\n")


# ==========================================
# 2. Geometric Complex Plane Visualization
# ==========================================
# Define the circular contour boundary (Unit Circle |z| = 1)
theta = np.linspace(0, 2 * np.pi, 400)
contour_x = np.cos(theta)
contour_y = np.sin(theta)

fig, ax = plt.subplots(figsize=(8, 8))

# 2a. Draw the Area of Integration and Bounds
# Area filled in Light Blue
ax.fill(contour_x, contour_y, color='lightblue', alpha=0.4, label='Area of Integration ($|z| \leq 1$)')
# Bounds highlighted in Light Red
ax.plot(contour_x, contour_y, color='lightcoral', linewidth=3, label='Integral Bounds ($|z|=1$)')

# 2b. Overlay a 2D Magnitude Map of the Characteristic Function
# Create a grid over the complex plane to evaluate the magnitude of g(z)
X, Y = np.meshgrid(np.linspace(-1.3, 1.3, 200), np.linspace(-1.3, 1.3, 200))
Z = X + 1j * Y

# Convert the symbolic integrand into a fast numerical function for mapping
g_num = sp.lambdify(z, integrand, 'numpy')
magnitude = np.abs(g_num(Z))

# Clip extreme magnitudes near poles to keep the map readable
magnitude_clipped = np.clip(magnitude, 0, 15)

# Plot magnitude contours to visualize the structure of the function
contour_slices = ax.contour(X, Y, magnitude_clipped, levels=12, cmap='plasma', alpha=0.45, linewidths=1)
ax.clabel(contour_slices, inline=True, fontsize=8, fmt='%.1f')

# 2c. Plot the active poles inside the domain
for idx, p in enumerate(valid_poles):
    ax.scatter(p.real, p.imag, color='red', s=120, zorder=5, 
               label=f'Pole {idx+1}: {p.real:.1f} + {p.imag:.1f}j\nRes = {complex(residues[idx]):.2f}' if idx==0 else f'Pole {idx+1}: {p.real:.1f} + {p.imag:.1f}j')

# Grid alignment and axes aesthetic
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_xlabel('Real Axis ($\mathcal{Re}$)')
ax.set_ylabel('Imaginary Axis ($\mathcal{Im}$)')
ax.set_title('Residue Integration with Multiple Interior Poles', fontsize=12, fontweight='bold')
ax.set_aspect('equal', 'box')
ax.grid(True, which='both', alpha=0.2)
ax.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.show()
 

