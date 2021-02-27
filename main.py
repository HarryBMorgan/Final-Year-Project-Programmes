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

# Call read_emsa_file.py module to get the information from the .emsa file.
line = xrf.read_emsa_file("EDS_1.emsa")

# Call extract_info.py to get header information and data.
header_list, data_loc = xrf.extract_headers(line)
spectrum_data = xrf.extract_data(line, data_loc)

# Locate "#XPERCHAN" and "#OFFSET".
XPERCHAN = xrf.locate_header_info(header_list, "#XPERCHAN")
OFFSET = xrf.locate_header_info(header_list, "#OFFSET")

# Create Energy list.
Energy = []
for i in range(1, len(spectrum_data) + 1):
    Energy.append(i * XPERCHAN + OFFSET)

# Plot the Energy against the Intensit (spectrum_data).
plt.plot(Energy, spectrum_data)
plt.xlabel("Energy, eV"); plt.ylabel("Intensity, log-scale")
plt.xlim(0, 7500); plt.yscale('log')
plt.title("EDS 1 XRF Data")
plt.show()