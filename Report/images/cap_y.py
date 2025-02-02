import numpy as np
import matplotlib.pyplot as plt

# Data: acceleration (a_y) in g and capacitance in Farads
a_y = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
capacitance_y = np.array([
    1.5653953632810892E-16, 1.5653953632810907E-16, 1.565395364125613E-16,
    1.5653953649703286E-16, 1.5653953658152314E-16, 1.565395366660314E-16,
    1.5653953675055986E-16, 1.5653953683510648E-16, 1.565395369196712E-16,
    1.5653953700425743E-16, 1.5653953708886082E-16
])

# Convert capacitance to attofarads (1E-18)
capacitance_y_af = capacitance_y * 1e18

# Plot
plt.figure(figsize=(10, 6))
plt.plot(a_y, capacitance_y_af, marker='o', linestyle='-', color='b', label="Y-Load Capacitance")

# Labels and Title
plt.xlabel("Acceleration a_y (g)")
plt.ylabel("Capacitance (attofarads, aF)")
plt.title("Capacitance vs. Y-Load Acceleration")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show Plot
plt.show()

