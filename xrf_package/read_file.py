# -----------------------------------------------------------------------------
# read_file.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module reads the data from an EMSA/MAS Spectral Data File.
# It then creates a list of strings that represent each line in the list.

# -----------------------------------------------------------------------------
# FUNCTIONS
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
# MAIN
if __name__ == "__main__":
    # Call read function.
    Line = read_emsa_file("EDS_1.emsa")
    
    # Print line list to check the data is there.
    for i in Line:
        print(i)