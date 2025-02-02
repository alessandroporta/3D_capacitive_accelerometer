from mpmath import mp
from scipy.constants import epsilon_0

# Set precision (e.g., 50 decimal places)
mp.dps = 50

# ANALYTICAL CALCULATION
w = 50e-9  
dl = 25e-9
dt1 = 25e-9
dt2 = 165e-9
t = 135e-9
h = 40e-9
epsi = epsilon_0

# Static Capacitance Calculation
cl = epsilon_0 * (t * h) / dl
ct1 = epsilon_0 * (w * h) / dt1
ct2 = epsilon_0 * (w * h) / dt2

c_static = (2 * cl + ct1 + ct2)
c_static_tot = 12 * c_static

# Variable Capacitance
y = 46.32e-15  # Displacement variation

cl1_var = epsilon_0 * (t * h) / (dl - y)
cl2_var = epsilon_0 * (t * h) / (dl + y)

c_var = (cl1_var + cl2_var + ct1 + ct2)
c_var_tot = 12 * c_var

# Differences and Percentage Change
delta = (c_var_tot - c_static_tot)
delta_perc = 100 * (c_var_tot - c_static_tot) / c_static_tot

# Print Analytical Results
print(f"cl = {cl}")
print(f"ct1 = {ct1}")
print(f"ct2 = {ct2}")
print(f"c_static = {c_static}")
print(f"c_static_tot = {c_static_tot}")
print(f"cl1_var = {cl1_var}")
print(f"cl2_var = {cl2_var}")
print(f"c_var = {c_var}")
print(f"c_var_tot = {c_var_tot}")
print(f"delta = {delta}")
print(f"delta_perc = {delta_perc}%")

# SIMULATION
# Capacitance values at different accelerations (a_y)
capacitances = {
    0: 1.5653953632810892E-16,
    20: 1.5653953632810907E-16,
    40: 1.565395364125613E-16,
    60: 1.5653953649703286E-16,
    80: 1.5653953658152314E-16,
    100: 1.565395366660314E-16,
    120: 1.5653953675055986E-16,
    140: 1.5653953683510648E-16,
    160: 1.565395369196712E-16,
    180: 1.5653953700425743E-16,
    200: 1.5653953708886082E-16,
}

# Calculate Changes
cap_changes = {
    a: (capacitances[a] - capacitances[0]) for a in capacitances
}

percentage_changes = {
    a: (capacitances[a] - capacitances[0]) / capacitances[0] * 100 for a in capacitances
}

# Print Simulation Results
print("\nCapacitances (F):")
for a, c in capacitances.items():
    print(f"a_y = {a}g: {c} F")

print("\nCapacitance changes from c_0 (F):")
for a, change in cap_changes.items():
    print(f"a_y = {a}g: {change} F")

print("\nPercentage changes from c_0 (%):")
for a, change in percentage_changes.items():
    print(f"a_y = {a}g: {change}%")
