import numpy as np
import matplotlib.pyplot as plt

# Data: acceleration (a_x) in g and capacitance in Farads
a_x = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
capacitance_x = np.array([
    1.2788877863625221E-16, 1.2788877863625138E-16, 1.2788877862890484E-16,
    1.2788877862155998E-16, 1.2788877861421664E-16, 1.278887786068754E-16,
    1.278887785995367E-16, 1.2788877859219939E-16, 1.278887785848652E-16,
    1.278887785775316E-16, 1.2788877857020074E-16
])

# Convert capacitance to attofarads (1E-18)
capacitance_x_af = capacitance_x * 1e18

# Plot
plt.figure(figsize=(10, 6))
plt.plot(a_x, capacitance_x_af, marker='o', linestyle='-', color='r', label="X-Load Capacitance")

# Labels and Title
plt.xlabel("Acceleration a_x (g)")
plt.ylabel("Capacitance (attofarads, aF)")
plt.title("Capacitance vs. X-Load Acceleration")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show Plot
plt.show()
