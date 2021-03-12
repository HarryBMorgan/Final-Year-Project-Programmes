# -----------------------------------------------------------------------------
# extract_info.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module extracts the headers from a file input.
# The file extracts the data usig read_emsa_file.py module.
# These headers are organised into a dictionary and returned to user.

# -----------------------------------------------------------------------------
# FUNCTIONS
def extract_emsa_headers(list):
# This function extracts the header information from a .emsa file type. Each
# line is formatted and stored in a list for output.
    
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
    array_one = []
    array_two = []
    
    # Run through list from data_loc to end.
    for i, val in enumerate(list[data_loc + 1: len(list)]):
    
        # Set data.
        data = val.split()
        
        try:
        
            # Take data and make each column into number.
            array_one.append(float("".join(j for j in data[0] if \
                            (j.isdigit() or j == "." or j == "E" or \
                            j == "e" or j == "-" or j == "+"))))
            
            array_two.append(float("".join(j for j in data[-1] if \
                            (j.isdigit() or j == "." or j == "E" or \
                            j == "e" or j == "-" or j == "+"))))
        
        except:
            # End of data.
            pass
        
    return array_one, array_two

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
        return header_stripped, info_float
    
    except ValueError:
        
        # If can't convert to float, return header & info.
        return header_stripped, info_stripped

# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    # Define test input.
    list = ["#Poop : Yummy!", "##Anna : 21.5", "#SPECTRUM :", \
            "0.5", "1.111", "64", "0.335", "#END : Test"]
    
    # Call the functions.
    header_list, data_loc = extract_emsa_headers(list)
    Energy, spectrum_data = extract_data(list, data_loc)
    
    # Print to the user.
    for i in range(len(header_list)):
        print(header_list[i][0], header_list[i][1])
    
    # Print information to the user.
    print(spectrum_data)