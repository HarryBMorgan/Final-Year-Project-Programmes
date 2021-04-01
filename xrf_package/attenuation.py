# -----------------------------------------------------------------------------
# attenuation.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module extracts the data from an attenuation file and calculates the
# amount of attenuation through the material.

# -----------------------------------------------------------------------------
# IMPORTS
from xrf_package.read_file import read_file
from xrf_package.extract_info import extract_data
from bisect import bisect_right
from math import exp

# -----------------------------------------------------------------------------
# FUNCTIONS
def attenuation(File, Energy):
# This function calculates the attenuation of the beam through the sample. The
# inputs are the File name as a string, the Energy of the peak in keV, and the
# attenuation depth X in cm.

    # Read in data.
    Atten_data = read_file(File)
    
    # Extract data.
    Atten_E, Atten = extract_data(Atten_data, 2)
    
    # Find index of attenuation of beam energy - multiply by 1e-3 to get from
    # keV to MeV.
    Indx = bisect_right(Atten_E, Energy * 1e-3) - 1
    
    # Define density, Rho, and depth, X.
    Rho = 4.1 # g/cm**3
    X = 0.1 # cm
    
    # Append to list of attenuations.
    Attenuation = exp(- Atten[Indx] * Rho * X)
    
    return Attenuation

# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    pass