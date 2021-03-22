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
from math import sqrt
from bisect import bisect_right
import xrf_package.xrf_package as xrf


            # ---           VARIABLES           --- #
# Contained here are the file names and gates within which the peaks reside.
# The peak gate limits are in units of keV.

# Information for the EDS_1 data.
file_name = "EDS_1.emsa"
X_lim = [[1.430, 1.630], [2.260, 2.550], [2.550, 2.750], [4.190, 4.430]]
Fluorescence_shell = ["wl", "wm", "wk", "wl"]
axis_upper_lim = 10

# Common variables.
Element = ["Br", "Pb", "Cl", "Cs"]
Atten_files = ["Br_attenuation.txt", "Pb_attenuation.txt", \
                "Cl_attenuation.txt", "Cs_attenuation.txt"]


            # ---           DATA EXTRACTION         --- #
# This section takes the headers and data from the spectrum file. It is then
# sorted and formatted.

# Call read_emsa_file.py module to get the information from the .emsa file.
file_data = xrf.read_file(file_name)

# Call extract_info.py to get header information and data.
header_list, data_loc = xrf.extract_emsa_headers(file_data)
Energy, spectrum_data = xrf.extract_data(file_data, data_loc)

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


            # ---           DATA VISUALISATION          --- #
# Create Energy list if the output from extract_data are equal. (In this case
# there is no energy column and one is required.)
if Energy == spectrum_data:
    Energy = []
    
    for i in range(1, len(spectrum_data) + 1):
        Energy.append(i * XPERCHAN + OFFSET)

# Plot the Energy against the Intensities (spectrum_data).
plt.plot(Energy, spectrum_data)
plt.xlabel("Energy, keV", fontsize = 20)
plt.ylabel("Intensity, log-scale", fontsize = 20)
plt.xlim(0, axis_upper_lim)
plt.yscale('log')
plt.title(file_name + ": XRF Data", fontsize = 20)
#plt.show()


            # ---           DATA ANALYSIS           --- #
# This section creates data such as the integrated value, fluorescence yield 
# and attenuation - only if there is information to analyise.

# Integrate over the peak defined using the integrate_peak module.
count, count_err = [], []
for i, val in enumerate(X_lim):
    count.append(xrf.integrate_peak(val, Energy, spectrum_data))
    count_err.append(sqrt(count[-1]))

# Find Energy for each peak using the peak_energy module.
Peak_energy = []
for i, val in enumerate(X_lim):
    Peak_energy.append(xrf.peak_energy(val, Energy, spectrum_data))

# True number of atoms.
Flu_yield = []
for i, val in enumerate(count):
    Flu_yield.append(xrf.fluorescence_yield(Element[i], Fluorescence_shell[i]))

Atom_num = []
for i, val in enumerate(count):
    Atom_num.append(val / Flu_yield[i])

# Total number of atoms is calculated.
Atom_tot = sum(Atom_num)

# % of sample.
Amount = []
for i in Atom_num:
    Amount.append(i / Atom_tot * 100)

# Get beam energy in MeV from headers.
BEAM = xrf.locate_list_element(header_list, "#BEAMKV   -kV")

# Get attenuation data.
Attenuation = []
for i, val in enumerate(Atten_files):
    Attenuation.append(xrf.attenuation(val, Peak_energy[i], 1))


            # ---           DATA VISUALISATION          --- #
# Pring tdata table of results.
print("")
print("  :" + "  Energy   :" + \
        "        Int       :" + \
        "   Fluorescence Yield   :" + \
        "   Attenuation   :" + \
        "  % of Sample  :")
for i, val in enumerate(Element):
    
    print(val + ": " + str('%.2f' %Peak_energy[i]) + " keV  : " + \
            str('%.2e' %count[i]) + " +/- " + str('%.0f' %count_err[i]) + \
            " :         " + str('%.4f' %Flu_yield[i]) + \
            "         :   " + str('%.2f' %Attenuation[i]) + " cm\u00b2/g   :" + \
            "    " + str('%.2f' %Amount[i]) + " %     :")

# Print information about experimental setup.
print("")
print("Data from", file_name)
print("Incident beam voltage =", BEAM, "kV")