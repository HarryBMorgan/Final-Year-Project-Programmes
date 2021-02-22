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
import numpy as np
import matplotlib.pyplot as plt
import xrf_package.xrf_package as xrf

# Call extract_info.py module to get the headers and data lists.
header_list, spectrum_data = xrf.extract_info(True, "EDS_1.emsa")

# Locate "#XPERCHAN" and "#OFFSET".
XPERCHAN = xrf.locate_header_info(header_list, "#XPERCHAN")
OFFSET = xrf.locate_header_info(header_list, "#OFFSET")

# Create Energy list.
Energy = []
for i in range(1, len(spectrum_data) + 1):
    Energy.append(i * XPERCHAN[-1] + OFFSET[-1])

# Plot the Energy against the Intensit (spectrum_data).
plt.plot(Energy, spectrum_data)
plt.xlabel("Energy, eV"); plt.ylabel("Intensity, log-scale")
plt.xlim(0, 7500); plt.yscale('log')
plt.title("EDS 1 XRF Data")
plt.show()