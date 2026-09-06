import numpy as np
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


"""
Note:
Characteristic Function: Expresses the singular map \(g(z)\) capturing geometric weights before collapsing to a scalar boundary map (\(2\pi i \cdot e^{0.5}\)) upon integration.
"""