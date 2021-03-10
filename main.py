# -----------------------------------------------------------------------------
# xrf analysis
# main.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module acts as the main of the XRF analysis programme.
# It utalises the xrf_package to take data from a .emsa file type and plots
# this data on a graph of energy vs intensity.

# -----------------------------------------------------------------------------
# MAIN
# Import the modules.
import matplotlib.pyplot as plt
import xrf_package.xrf_package as xrf

# ---
# Call read_emsa_file.py module to get the information from the .emsa file.
#file_name = "S1-20kV-08nA-x100_pt1.psmsa"
file_name = "EDS_1.emsa"
line = xrf.read_emsa_file(file_name)

# Call extract_info.py to get header information and data.
header_list, data_loc = xrf.extract_headers(line)
spectrum_data = xrf.extract_data(line, data_loc)

# Locate "#XPERCHAN", "#OFFSET" and "XUNITS". Adjust values based on XUNITS.
# All Energy outputs will be in units of keV.
XUNITS = xrf.locate_list_element(header_list, "#XUNITS")
XPERCHAN = xrf.locate_list_element(header_list, "#XPERCHAN")
OFFSET = xrf.locate_list_element(header_list, "#OFFSET")

if XUNITS == "eV":
    XPERCHAN *= 1e-3
    OFFSET *= 1e-3
elif XUNITS == "keV":
    pass
elif XUNITS == "MeV":
    XPERCHAN *= 1e3
    OFFSET *= 1e3


# ---
# Create Energy list.
Energy = []
for i in range(1, len(spectrum_data) + 1):
    Energy.append(i * XPERCHAN + OFFSET)

# Manually input the X limits that act as the integration gates on the data.
# This is for the S1-20kV-08nA-x100_pt1.psmsa data.
#X_lim = [[1.41, 1.75], [10.42, 10.86]]
# This one is for the EDS_1.emsa data.
X_lim = [[1.430, 1.630], [2.260, 2.550], [2.550, 2.750], [4.190, 4.430]]

# Integrate over the peak defined using the integrate_peak module.
count = []
for i in X_lim:
    count.append(xrf.integrate_peak(i, Energy, spectrum_data))

# Find Energy for each peak using the peak_energy module.
Peak_energy = []
for i in X_lim:
    Peak_energy.append(xrf.peak_energy(i, Energy, spectrum_data))

# Print integrated values next to the element they represent.
element = ["Br", "Pb", "Cl", "Cs"]
print("     Energy       Int")
for i, val in enumerate(count):
    print(element[i] + ": " + str('%.2f' %Peak_energy[i]) + " keV   " + \
            str('%.2f' %val))


# ---
# Plot the Energy against the Intensit (spectrum_data).
plt.plot(Energy, spectrum_data)
plt.xlabel("Energy, keV"); plt.ylabel("Intensity, log-scale")
plt.xlim(0, 10); plt.yscale('log')
plt.title(file_name + ": XRF Data")
plt.show()