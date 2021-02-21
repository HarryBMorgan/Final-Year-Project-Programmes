# -----------------------------------------------------------------------------
# extract_info.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module extracts the headers from a list input of type string.
# These headers are organised into a dictionary and returned to user.

# -----------------------------------------------------------------------------
# IMPORT
import numpy as np

# -----------------------------------------------------------------------------
# CLASSES
# CREATE A CLASS TO HOLD HEADER DATA.

# -----------------------------------------------------------------------------
# FUNCTIONS
def extract_info(list):
# This function extracts the header information and spectrum data from the
# input list. The list will have been obtained via the read_emsa_file.py
# module. a list of the headers and an array of data will be passed to user.

    header_list, data_loc = extract_headers(list)
    spectrum_array = extract_data(list, data_loc)
    return header_list, spectrum_array

def extract_headers(list):

    # Read every element in list (represents lines from data file).
    header_list, spectrum_list = [], []
    for i in range(len(list)):

        # Check for "#". This means the element is a header.
        if list[i][0] == "#":
        # Run through the element and seperate header and info then format.

            # Run header extraction subroutine.
            header_new, info_new = __header_extraction__(list, i)

            # Check if header is begining the spectrum data.
            if "SPECTRUM" in header_new:

                # Set location in list of data. Exit function.
                data_loc = i
                break

            else:
            # Not begining of spectrum data, append to header_list.

                header_list.append([header_new, info_new])

        elif list[i][0] != "#":
            pass

    # Pass the data to the user.
    return header_list, data_loc

def extract_data(list, data_loc):
# This function extracts the data from the list and formats it to type float.

    # Read each line after "#SPECTRUM".
    spectrum_array = np.array(3)

    return spectrum_array

def __header_extraction__(list, i):
# This function runs the bullk of the extract_headers module.

    # Create temp string lists to be extract header & info.
    header, info = "", ""

    # Run through element to extract header name.
    j = 0
    while list[i][j] != ":":

        # Append header to header.
        header += list[i][j]

        # Incriment j.
        j += 1

    # Take info from element.
    for k in range(j, len(list[i])):
        # Append info to info.
        info += list[i][k]

    # Format header & information.
    header_new, info_new = __format_header__(header, info)
    return header_new, info_new

def __format_header__(header, info):
# This function formats the header and its information by removing any unneeded
# characters & whitespace. it converts info to other data type where required.

    # Remove ":" from strings.
    header_no_colon = header.replace(":", "")
    info_no_colon = info.replace(":", "")

    # Trim the whitespace from the header and its info.
    header_stripped = header_no_colon.strip()
    info_stripped = info_no_colon.strip()

    # Try converting the info to type float.
    try:

        # Try converting to float.
        info_float = float(info_stripped)

        # If successful return header & info_float.
        return header, info_float

    except ValueError:

        # If can't convert to float, return header & info.
        return header, info_stripped

# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    # Define test input.
    list = ["#Poop : Yummy!", "##Anna : 21.5", "#SPECTRUM :", "#END : Test"]

    # Call the function.
    header_list, data_loc = extract_headers(list)

    # Print to the user.
    for i in range(len(header_list)):
        print(header_list[i][0], header_list[i][1])