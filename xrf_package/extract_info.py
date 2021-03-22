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
def extract_emsa_headers(List):
# This function extracts the header information from a .emsa file type. Each
# line is formatted and stored in a list for output.
    
    # Read every Element in list (represents lines from data file).
    Header_list, Spectrum_list = [], []
    for i in range(len(List)):
        
        # Check for "#". This means the Element is a header.
        if List[i][0] == "#":
        # Run through the Element and seperate header and info then format.
            
            # Run header extraction subroutine.
            Header_new, Info_new = __header_extraction__(List, i)
            
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
            pass
        
    return Array_one, Array_two

def __header_extraction__(List, i):
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
    Header_new, Info_new = __format_header__(Header, Info)
    return Header_new, Info_new

def __format_header__(Header, Info):
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

# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    # Define test input.
    List = ["#Poop : Yummy!", "##Anna : 21.5", "#SPECTRUM :", \
            "0.5", "1.111", "64", "0.335", "#END : Test"]
    
    # Call the functions.
    Header_list, Data_loc = extract_emsa_headers(List)
    Energy, Spectrum_data = extract_data(List, Data_loc)
    
    # Print to the user.
    for i in range(len(Header_list)):
        print(Header_list[i][0], Header_list[i][1])
    
    # Print information to the user.
    print(Spectrum_data)