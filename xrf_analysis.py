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
from numpy import linspace, polyfit
import xrf_module as xrf


            # ---           VARIABLES           --- #
# Contained here are the file names and gates within which the peaks reside.
# The peak gate limits are in units of keV. The fluorescence shell is the shell
# which the fluorescence is generated. It is required to perform the
# fluorescence yield correction. The element and attenuation files are required
# to be written in the order they appear in the spectra.

# To first plot just the spectra all that is needed is the data file name. The
# plot command under # --- VISUALISATION --- # can be edited for a prefered
# format to the output, e.g., log/linear output, title, savefile name, etc.

# FAPbBr_40keV_powdered.Spe
File_name = "FAPbBr_40keV_powdered.Spe"
X_lim = [[10.20, 10.86], [11.54, 12.26]]
Fluorescence_shell = ["wl", "wk"]
Element = ["Pb", "Br"]
Atten_files = ["Pb_attenuation.txt", "Br_attenuation.txt"]
Actual_energy = [10.5515, 11.8776]


            # ---           EXTRACTION         --- #
# This section takes the headers and data from the spectrum file. It is then
# sorted and formatted. There is a check for which type the file is as there
# are different procedures to follow for each.

# Call read_ file.py module to get the information from the file.
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
        
        for i in range(len(Spectrum_data)):
            Energy.append(i * XPERCHAN + OFFSET)

# The extraction for Spe type files.
elif "Spe" in File_name:
    # Call extract_data to get data.
    Eh, Spectrum_data = xrf.extract_data(File_data, 12)

    # Create Energy list.
    Energy = []
    for i in range(8191):
        Energy.append(-0.029029 + i * 0.010367)


            # ---           VISUALISATION          --- #
# Plot the Energy against the Intensities (Spectrum_data).
plt.plot(Energy, Spectrum_data)
plt.xlabel("Energy, keV", fontsize = 12)
# plt.xlim(0, 40)
plt.ylabel("Intensity (log)", fontsize = 12)
plt.yscale("log")
plt.title(File_name.split(".")[0] + ": XRF Data", fontsize = 12)
plt.tight_layout()
# plt.savefig("Output/" + File_name.split(".")[0] + "_Spectrum.PNG")
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
    Flu_yield.append(xrf.fluorescence_yield(val, Fluorescence_shell[i]))

# Cacluate total number of atoms for each element in sample.
# Flourescence correction.
Atom_num, Atom_num_err = [], []
for i, val in enumerate(Count):
    Atom_num.append(val / Flu_yield[i])
    Atom_num_err.append(Atom_num[-1] * Count_err[i])
    # Atom_num.append(val / (Flu_yield[i] * Attenuation[i]))

# Calculate the ratio of PB:Halide and if its present, Br:Cl.
Ratio = xrf.lead_halide_ratio(Element, Atom_num)
if len(Ratio) == 1:
    print(Ratio[0])
elif len(Ratio) == 2:
    print(Ratio[0])
    print(Ratio[-1])

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
    "  % of Sample  :")

for i, val in enumerate(Element):
    try:
        print('%.2s' %val + \
            '%.13s' %(":  " + str('%.2f' %Peak_energy[i]) + " keV            ") + \
            '%.19s' %(": " + str('%.2e' %Count[i]) + " +/- " + \
                str('%.0f' %Count_err[i]) + "                                ") + \
            '%.21s' %(":       " + str('%.4f' %Flu_yield[i]) + "             ") + \
            '%.16s' %(":   " + str('%.2e' %Attenuation[i]) + "               ") + \
            '%.16s' %(":    " + str('%.2f' %Percent[i]) + " %                ") + \
            '%.1s' %":")
    except IndexError:
        break


            # ---           RESIDUAL PLOT           --- #
# This section will be for plotting the residual of the spectra.
# This is the difference between the measured and actual fluorescence energy.

# Create Residual data.
Residual = []
for i, val in enumerate(Actual_energy): Residual.append(val - Peak_energy[i])

plt.scatter(Actual_energy, Residual, marker = "x")
plt.title(File_name.split(".")[0] + ": Residual Plot", fontsize = 12)
plt.xlabel("Energy, keV", fontsize = 12)
plt.ylabel("Residual, keV", fontsize = 12)
plt.axhline(y = 0, color = "k", label = "y = 0")
plt.legend()
plt.tight_layout()
# plt.savefig("Output/" + File_name.split(".")[0] + "_Residual.PNG")
# plt.show()

# EXIT COMMAND
Exit = input("Hit ENTER to end program and exit:")