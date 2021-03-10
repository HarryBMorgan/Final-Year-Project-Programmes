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
# Contained here are the file names and gates within which the peaks reside.
# The peak gate limits are in units of keV.
#'''
# Information for the EDS_1 data.
file_name = "EDS_1.emsa"
X_lim = [[1.430, 1.630], [2.260, 2.550], [2.550, 2.750], [4.190, 4.430]]
Element = ["Br", "Pb", "Cl", "Cs"]
Fluorescence_shell = ["w1", "w3", "wk", "w1"]
axis_upper_lim = 10
#'''

'''
# Information for the S1_pt1 data.
file_name = "S1-20kV-08nA-x100_pt1.psmsa"
X_lim = [[1.41, 1.75], [10.42, 10.86]]
axis_lim = 20
Element = ["Br", "Pb"]
Fluorescence_shell = ["w1", "w1"]
axis_upper_lim = 20
'''


# ---
# Call read_emsa_file.py module to get the information from the .emsa file.
file_data = xrf.read_emsa_file(file_name)

# Call extract_info.py to get header information and data.
header_list, data_loc = xrf.extract_headers(file_data)
spectrum_data = xrf.extract_data(file_data, data_loc)

# Locate "#XPERCHAN", "#OFFSET" and "XUNITS". Adjust values based on XUNITS.
XPERCHAN = xrf.locate_list_element(header_list, "#XPERCHAN")
OFFSET = xrf.locate_list_element(header_list, "#OFFSET")
XUNITS = xrf.locate_list_element(header_list, "#XUNITS")

# All Energy outputs will be altered to be in units of keV.
if XUNITS == "eV":
    
    XPERCHAN *= 1e-3
    OFFSET *= 1e-3

elif XUNITS == "MeV":
    
    XPERCHAN *= 1e3
    OFFSET *= 1e3


# ---
# Create Energy list.
Energy = []
for i in range(1, len(spectrum_data) + 1):
    Energy.append(i * XPERCHAN + OFFSET)

# Integrate over the peak defined using the integrate_peak module.
count = []
for i in X_lim:
    count.append(xrf.integrate_peak(i, Energy, spectrum_data))

# Find Energy for each peak using the peak_energy module.
Peak_energy = []
for i in X_lim:
    Peak_energy.append(xrf.peak_energy(i, Energy, spectrum_data))

# Print integrated values next to the element they represent.
print("  :  Energy   :   Int    :   Fluorescence Yield   :   True # of Atoms :")
for i, val in enumerate(count):
    
    # Assign print variables from the various lists.
    a = Element[i]
    b = '%.2f' %Peak_energy[i]
    c = xrf.fluorescence_yield(Element[i], Fluorescence_shell[i])
    d = val / c
    
    print(a + ": " + str(b) + " keV  : " + str('%.2e' %val) + " :        " + \
            str('%.4f' %c) + "          :      " + str('%.2e' %d) + "     :")


# ---
# Plot the Energy against the Intensit (spectrum_data).
plt.plot(Energy, spectrum_data)
plt.xlabel("Energy, keV"); plt.ylabel("Intensity, log-scale")
plt.xlim(0, axis_upper_lim)
plt.yscale('log')
plt.title(file_name + ": XRF Data")
plt.show()