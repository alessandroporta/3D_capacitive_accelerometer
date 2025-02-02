import numpy as np
import matplotlib.pyplot as plt

# Data: angles (alpha) in radians and displacements in nm
alpha = np.array([0, np.pi/20, np.pi/10, 3*np.pi/20, np.pi/5, np.pi/4, 
                  3*np.pi/10, 7*np.pi/20, 2*np.pi/5, 9*np.pi/20, np.pi/2])
x_displacement = np.array([3.240466648790339E-5, 3.849951165974537E-5, 5.4894985291645114E-5, 
                           6.993871164061217E-5, 8.326677201067045E-5, 9.454813813604667E-5, 
                           1.0350138816950455E-4, 1.0990606042193493E-4, 1.1360454523737904E-4, 
                           1.1450632634594326E-4, 1.1258855274278644E-4]) * 1e9  # Convert to nm
y_displacement = np.array([6.999755627963146E-5, 7.278341711093986E-5, 7.377716493460282E-5, 
                           7.295433051022473E-5, 7.033517436690303E-5, 6.598418923855103E-5, 
                           6.000851051469656E-5, 5.255527931571971E-5, 4.511746179761701E-5, 
                           4.5950759554042796E-5, 4.63210427855019E-5]) * 1e9  # Convert to nm

# Convert alpha to fractions of pi for labels
alpha_labels = [r"$0$", r"$\frac{\pi}{20}$", r"$\frac{\pi}{10}$", r"$\frac{3\pi}{20}$", 
                r"$\frac{\pi}{5}$", r"$\frac{\pi}{4}$", r"$\frac{3\pi}{10}$", 
                r"$\frac{7\pi}{20}$", r"$\frac{2\pi}{5}$", r"$\frac{9\pi}{20}$", r"$\frac{\pi}{2}$"]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(alpha, x_displacement, label="X Displacement", marker="o", linestyle="-")
plt.plot(alpha, y_displacement, label="Y Displacement", marker="s", linestyle="--")

# Customize the plot
plt.xticks(alpha, alpha_labels)
plt.xlabel(r"$\alpha$ (Angle in radians, fractions of $\pi$)")
plt.ylabel("Displacement (nm)")
plt.title("Displacement vs. Angle of Acceleration")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
