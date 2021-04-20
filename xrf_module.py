# -----------------------------------------------------------------------------
# read_file.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# This module contains all the functions that are used for analysing data in
# the xrf program. They will all come with their own descriptions.

# -----------------------------------------------------------------------------
# IMPORTS
from numpy import linspace
from scipy.integrate import simps
from bisect import bisect_right
from math import exp

# -----------------------------------------------------------------------------
# READ FILE
# This module reads the data from an EMSA/MAS Spectral Data File.
# It then creates a list of strings that represent each line in the list.

def read_file(File_name):
# This function takes a string input. This must be either the directory of the
# data file or the name of the file (if it is in the same directory as the
# module).
# The output is a list string of type string. Each Element is a line in the
# data file.

    # Open data file.
    Data_file = open(File_name, "r")
    
    # Extract lines into list.
    Line = Data_file.readlines()
    
    # Close the data file.
    Data_file.close
    
    # Give the line list back to the user.
    return Line

# -----------------------------------------------------------------------------
# EXXTRACT INFORMATION
# These fuctions are for extracting information from the data files and
# formatting them into something that is usable by the program.

def extract_msa_headers(List):
# This function extracts the header information from a .msa file type. Each
# line is formatted and stored in a list for output.
    
    # Read every Element in list (represents lines from data file).
    Header_list = []
    for i in range(len(List)):
        
        # Check for "#". This means the Element is a header.
        if List[i][0] == "#":
        # Run through the Element and seperate header and info then format.
            
            # Run header extraction subroutine.
            Header_new, Info_new = __msa_header_extraction__(List, i)
            
            # Check if header is begining the spectrum data.
            if "SPECTRUM" in Header_new:
                
                # Set location in list of data. Exit function.
                Data_loc = i
                break
            
            else:
            # Not begining of spectrum data, append to Header_list.
                
                Header_list.append([Header_new, Info_new])
            
        elif List[i][0] != "#":
            pass
        
    # Pass the data to the user.
    return Header_list, Data_loc

def __msa_header_extraction__(List, i):
# This function runs the bullk of the extract_headers module.
    
    # Create temp string lists to be extract header & info.
    Header, Info = "", ""
    
    # Run through Element to extract header name.
    j = 0
    while List[i][j] != ":":
    
        # Append header to header.
        Header += List[i][j]
        
        # Incriment j.
        j += 1
    
    # Take info from Element.
    for k in range(j, len(List[i])):
        # Append info to info.
        Info += List[i][k]
    
    # Format header & information.
    Header_new, Info_new = __format_msa_header__(Header, Info)
    return Header_new, Info_new

def __format_msa_header__(Header, Info):
# This function formats the header and its information by removing any unneeded
# characters & whitespace. it converts info to other data type where required.
    
    # Remove ":" from strings.
    Header_no_colon = Header.replace(":", "")
    Info_no_colon = Info.replace(":", "")
    
    # Trim the whitespace from the header and its info.
    Header_stripped = Header_no_colon.strip()
    Info_stripped = Info_no_colon.strip()
    
    # Try converting the info to type float.
    try:
        
        # Try converting to float.
        Info_float = float(Info_stripped)
        
        # If successful return header & info_float.
        return Header_stripped, Info_float
    
    except ValueError:
        
        # If can't convert to float, return header & info.
        return Header_stripped, Info_stripped

def extract_data(List, Data_loc):
# This function extracts the data from the list and formats it to type
# float. This is then output to the user. The function tries splitting the str
# into 2 columns. The second array is populated by the end of data list,
# data[-1], to prevent error if there is only one column in the list. The
# inputs are the list of strigs, directly from the file, and the location at
# which to start looking for the data, as an int. The programme reaches the end
# of file when it can no longer convert to floats, as handled by except. The
# arrays are returned to the user. The assignment of what they represent
# should be known by the user (i.e. Energy, spectrum data,
# fluorescence yield, etc.).
    
    # Create array to hold data.
    Array_one = []
    Array_two = []
    
    # Run through list from Data_loc to end.
    for i, val in enumerate(List[Data_loc + 1: len(List)]):
    
        # Set data.
        Data = val.split()
        
        try:
        
            # Take data and make each column into number.
            Array_one.append(float("".join(j for j in Data[0] if \
                            (j.isdigit() or j == "." or j == "E" or \
                            j == "e" or j == "-" or j == "+"))))
            
            Array_two.append(float("".join(j for j in Data[-1] if \
                            (j.isdigit() or j == "." or j == "E" or \
                            j == "e" or j == "-" or j == "+"))))
        
        except:
            # End of data.
            break
        
    return Array_one, Array_two

# -----------------------------------------------------------------------------
# LOCATE LIST ELEMENT
# This module locates the position of a header in a list.
# It provides the information to the user.

def locate_list_element(List, Element):
# Search the list for the specified Element. Once found it will be returned to
# the user.
# WARNING! This module's "Element" input is case sensitive.

    try:
    
        Position = [val[-1] for i, val in enumerate(List) if val[0] == Element]
        
        return Position[0]
    
    except:
    
        print("ERROR: Element not found. Check input is exact.")

# -----------------------------------------------------------------------------
# EVALUATE PEAK
# This programme integrates and finds the max energy of a spectal peak provided
# by user input.

def peak_energy(X_lim, X_data, Y_data):
# This function finds the peak energy for the peak defined by the parameters.
    
    # Create X_lim index.
    a = bisect_right(X_data, X_lim[0]) - 1
    b = bisect_right(X_data, X_lim[-1]) - 1
    
    # Find index of max value in Y_data.
    Indx = Y_data[a: b].index(max(Y_data[a: b])) + a
    
    # Find associated x_coordinate and return to user.
    return X_data[Indx]
 
def integrate_peak(X_lim, X_data, Y_data):
# This function finds the value of the integral below the peak enclosed within
# the boundaries set by the X_lim input. The input N allows for the user to
# decide between speed and accuracy for the integral.

    # Create X_lim index.
    a = bisect_right(X_data, X_lim[0]) - 1
    b = bisect_right(X_data, X_lim[-1]) - 1

    # Remove baseline from Y_data.
    Y_data_lowered = __remove_baseline__(a, b, X_data, Y_data)
    
    # Integrate using Simpsons Rule from SciPy.
    Count = simps(Y_data_lowered)
    
    # Return the integrated value to the user.
    return Count

def __remove_baseline__(a, b, X_data, Y_data):
# This function generates a baseline reading of a straight line between the
# upper and lower x limits and subtracts it from the Y_data.

    # Create baseline.
    Baseline = linspace(Y_data[a], Y_data[b], len(Y_data[a: b+1]))

    # Subtract Baseline and return to user.
    return Y_data[a: b+1] - Baseline

# -----------------------------------------------------------------------------
# FLUORESECNCE YIELD
# This module locates the correct fluorescence yield and returns it to user.

def fluorescence_yield(Element, Yield):
# This function takes the Elemental symbol and shell designation (e.g. "Br", 
# "w1") as type str and returns the fluorescence yield for that Element at
# that shell.

    Fluorescence_dict = {"Br wk": 0.6275, "Br wl": 0.0195, "Br wm": 3.02e-4, \
                    "Pb wk": 0.9634, "Pb wl": 0.369, "Pb wm": 0.0292, \
                    "Cl wk": 0.09892, "Cl wl": 0.00118, \
                    "Cs wk": 0.8942, "Cs wl": 0.0938, "Cs wm": 0.00401}
    
    # Find which yield we're talking about and return it to the user.
    return Fluorescence_dict[Element + " " + Yield]

# -----------------------------------------------------------------------------
# ATTENUATION
# This module extracts the data from an attenuation file and calculates the
# amount of attenuation through the material.

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