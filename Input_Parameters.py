# -----------------------------------------------------------------------------
# xrf analysis
# Input_Parameters.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This file acts as a store for the different input parameters I have used/will
# use. They can be copied into the main.py in place of the current parameters
# where necessary.

# Contained here are the file names and gates within which the peaks reside.
# The peak gate limits are in units of keV.
# The fluorescence shell is the shell which the fluorescence is generated.
# It is required to perform the fluorescence yield correction.
# The element and attenuation files are required to be written in the order
# they appear in the spectra.
# The Actuall_energy is for calculating the residual plot. These values should
# be from tables and be in the same order as the elements appear in the
# spectra. They should also be in units of keV.


# EDS_1.emsa
File_name = "EDS_1.emsa"
X_lim = [[4.19, 4.43], [2.26, 2.55], [1.42, 1.62], [2.55, 2.78]]
Fluorescence_shell = ["wl", "wm", "wl", "wk"]
Element = ["Cs", "Pb", "Br", "Cl"]
Atten_files = ["Cs_attenuation.txt", "Pb_attenuation.txt", \
    "Br_attenuation.txt", "Cl_attenuation.txt"]
Actual_energy = [4.2865, 2.3455, 1.48043, 2.62078]

# S1-20kV-08nA-x100_pt1.psmsa
File_name = "S1-20kV-08nA-x100_pt1.psmsa"
X_lim = [[2.26, 2.58], [1.41, 1.69]]
Fluorescence_shell = ["wm", "wl"]
Element = ["Pb", "Br"]
Atten_files = ["Pb_attenuation.txt", "Br_attenuation.txt"]
Actual_energy = [2.3455, 1.4843]

# FAPbBr_40keV_powdered.Spe
File_name = "FAPbBr_40keV_powdered.Spe"
X_lim = [[10.20, 10.86], [11.54, 12.26]]
Fluorescence_shell = ["wl", "wk"]
Element = ["Pb", "Br"]
Atten_files = ["Pb_attenuation.txt", "Br_attenuation.txt"]
Actual_energy = [10.5515, 11.8776]

# FAPbBr_40keV_crystal.Spe
File_name = "FAPbBr_40keV_crystal.Spe"
X_lim = [[10.16, 10.84], [11.54, 12.26]]
Fluorescence_shell = ["wl", "wk"]
Element = ["Pb", "Br"]
Atten_files = ["Pb_attenuation.txt", "Br_attenuation.txt"]
Actual_energy = [10.5515, 11.8776]

# CuRuMo_calibration.Spe
File_name = "CuRuMo_calibration.Spe"
X_lim = [[], []]
Fluorescence_shell = ["", ""]
Element = ["", ""]
Atten_files = ["", ""]
Actual_energy = []

# Pb_Calibration_Check.Spe
File_name = "Pb_Calibration_Check.Spe"
X_lim = [[10.19, 10.89], [12.08, 13.08]]
Fluorescence_shell = ["wl", "wl"]
Element = ["Pb", "Pb"]
Atten_files = ["Pb_attenuation.txt", "Pb_attenuation.txt"]
Actual_energy = [10.5515, 12.6137]