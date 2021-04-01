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
from numpy import linspace
import xrf_package.xrf_package as xrf


            # ---           VARIABLES           --- #
# Contained here are the file names and gates within which the peaks reside.
# The peak gate limits are in units of keV.

# EDS_1.emsa
# File_name = "EDS_1.emsa"
# X_lim = [[1.42, 1.62], [2.26, 2.55], [2.55, 2.78], [4.19, 4.43]]
# Fluorescence_shell = ["wl", "wm", "wk", "wl"]
# Y_scale = "log"
# Axis_upper_lim = 10

# S1-20kV-08nA-x100_pt1.psmsa
# File_name = "S1-20kV-08nA-x100_pt1.psmsa"
# X_lim = [[1.41, 1.69], [2.26, 2.58]]
# Fluorescence_shell = ["wl", "wm"]
# Y_scale = "log"
# Axis_upper_lim = 20

# FAPbBr_40keV_powdered.Spe
# File_name = "FAPbBr_40keV_powdered.Spe"
# Beam_eV = 40 # keV
# # X_lim = [[], []]
# Fluorescence_shell = ["wl", "wm"]
# Y_scale = "linear"
# Axis_upper_lim = 20

# FAPbBr_40keV_crystal.Spe
File_name = "FAPbBr_40keV_crystal.Spe"
Beam_eV = 40 # keV
# X_lim = [[], []]
Fluorescence_shell = ["wl", "wm"]
Y_scale = "linear"
Axis_upper_lim = 20

# Common variables.
Element = ["Br", "Pb", "Cl", "Cs"]
Atten_files = ["Br_attenuation.txt", "Pb_attenuation.txt", 
                "Cl_attenuation.txt", "Cs_attenuation.txt"]


            # ---           EXTRACTION         --- #
# This section takes the headers and data from the spectrum file. It is then
# sorted and formatted. There is a check for which type the file is as there
# are different procedures to follow for each.

# Call read_file.py module to get the information from the file.
File_data = xrf.read_file(File_name)

# The extraction for msa type files.
if "msa" in File_name:
    # Call extract_info.py to get header information and data.
    Header_list, Data_loc = xrf.extract_msa_headers(File_data)
    Energy, Spectrum_data = xrf.extract_data(File_data, Data_loc)

    # Locate "#XPERCHAN", "#OFFSET" and "XUNITS". Adjust values based on XUNITS.
    XPERCHAN = xrf.locate_list_element(Header_list, "#XPERCHAN")
    OFFSET = xrf.locate_list_element(Header_list, "#OFFSET")
    XUNITS = xrf.locate_list_element(Header_list, "#XUNITS")

    # All Energy outputs will be altered to be in units of keV.
    if XUNITS == "eV":
        XPERCHAN *= 1e-3
        OFFSET *= 1e-3

    elif XUNITS == "MeV":
        XPERCHAN *= 1e3
        OFFSET *= 1e3

    # Create Energy list if the output from extract_data are equal. (In this case
    # there is no energy column and one is required.)
    if Energy == Spectrum_data:
        Energy = []
        
        for i in range(1, len(Spectrum_data) + 1):
            Energy.append(i * XPERCHAN + OFFSET)

# The extraction for Spe type files.
elif "Spe" in File_name:
    # Call extract_data to get data.
    Eh, Spectrum_data = xrf.extract_data(File_data, 12)

    # Create Energy list.
    Energy = linspace(0, Beam_eV, len(Spectrum_data))


            # ---           VISUALISATION          --- #
# Plot the Energy against the Intensities (Spectrum_data).
plt.plot(Energy, Spectrum_data)
plt.xlabel("Energy, keV", fontsize = 20)
plt.ylabel("Intensity (" + Y_scale + ")", fontsize = 20)
plt.xlim(0, Axis_upper_lim)
plt.ylim(0, max(Spectrum_data) + max(Spectrum_data) / 10)
plt.yscale(Y_scale)
plt.title(File_name + ": XRF Data", fontsize = 20)
plt.show()


            # ---           ANALYSIS           --- #
# This section creates data such as the integrated value, fluorescence yield 
# and attenuation - only if there is information to analyise.

# Integrate over the peak defined using the integrate_peak module.
Count, Count_err = [], []
for i, val in enumerate(X_lim):
    Count.append(xrf.integrate_peak(val, Energy, Spectrum_data))
    Count_err.append(sqrt(Count[-1]))

# Find Energy for each peak using the peak_energy module.
Peak_energy = []
for i, val in enumerate(X_lim):
    Peak_energy.append(xrf.peak_energy(val, Energy, Spectrum_data))

# Get attenuation data.
Attenuation = []
for i, val in enumerate(Atten_files):
    try:
        Attenuation.append(xrf.attenuation(val, Peak_energy[i]))
    except IndexError:
        break

# True number of atoms.
Flu_yield = []
for i, val in enumerate(Element):
    try:
        Flu_yield.append(xrf.fluorescence_yield(val, Fluorescence_shell[i]))
    except IndexError:
        break

Atom_num, Atom_num_err = [], []
for i, val in enumerate(Count):
    Atom_num.append(val / Flu_yield[i])
    Atom_num_err.append(Atom_num[-1] * Count_err[i])
    # Atom_num.append(val / (Flu_yield[i] * Attenuation[i]))

# Ratio of Br to Cl.
try:
    X_Br = '%.2f' %(Atom_num[0] / (Atom_num[0] + Atom_num[2]))
    X_Cl = '%.2f' %(Atom_num[2] / (Atom_num[0] + Atom_num[2]))
    X = [X_Br, "    ", X_Cl, "    "]
except IndexError:
    X = ["    ", "    ", "    ", "    "]

# Total number of atoms is calculated.
Atom_tot = sum(Atom_num)

# % of sample.
Percent = []
for i in Atom_num:
    Percent.append(i / Atom_tot * 100)


            # ---           VISUALISATION 2.0          --- #
# Print data table of results.
print("  :" + \
    "   Energy   :" + \
    "       Int        :" + \
    " Fluorescence Yield :" + \
    "  Attenuation  :" + \
    "  % of Sample  :" + \
    "  Halide Ratio  :")

for i, val in enumerate(Element):
    try:
        print('%.2s' %val + \
            '%.13s' %(":  " + str('%.2f' %Peak_energy[i]) + " keV            ") + \
            '%.19s' %(": " + str('%.2e' %Count[i]) + " +/- " + \
                str('%.0f' %Count_err[i]) + "                                ") + \
            '%.21s' %(":       " + str('%.4f' %Flu_yield[i]) + "             ") + \
            '%.16s' %(":   " + str('%.2e' %Attenuation[i]) + "               ") + \
            '%.16s' %(":    " + str('%.2f' %Percent[i]) + " %                ") + \
            '%.17s' %(":      " + str(X[i]) + "                              ") + \
            '%.1s' %":")
    except IndexError:
        break