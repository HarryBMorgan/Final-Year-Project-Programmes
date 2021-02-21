# -----------------------------------------------------------------------------
# extract_headers.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module extracts the headers from a list input of type string.
# These headers are organised into a dictionary and returned to user.

# -----------------------------------------------------------------------------
# CLASSES
# CREATE A CLASS TO HOLD HEADER DATA.

# -----------------------------------------------------------------------------
# FUNCTIONS
def extract_headers(list):

    # Read every element in list (represents lines from data file).
    for i in range(len(list)):

        # Check for "#". This means the element is a header.
        if list[i][0] == "#":
        # Run through the element and seperate header and info then format.

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
            for l in range(j, len(list[i])):
                # Append info to info.
                info += list[i][l]

            # Remove ":" from strings.
            header_new = header.replace(":", "")
            info_new = info.replace(":", "")

            # Delete header & info from memory (reducing variables).
            del header, info

            # Trim the whitespace from the header and its info.
            header = header_new.strip()
            info = info_new.strip()

            # Try making the info into a float.
            try:

                # Try converting to float.
                info_float = float(info)

                # If successful print header & info_float.
                print(header, info_float)

            except ValueError:

                # If can't convert to float, print header & info.
                print(header, info)

        elif list[i][0] != "#":
            pass

    # Pass the data to the user.
    return

# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    # Define test input.
    list = ["#Poop : Yummy!", "##Anna : 69", "0.135,", "#END of : Test"]

    # Call the function.
    data_dict = extract_headers(list)

    # Print to the user.
    print(data_dict)

# -----------------------------------------------------------------------------
# METHOD
# Read the lines in the list. I guess look for the #.
# If # is there, take everything up to ":" then strip whitespace.
# Then take rest from after ":".
# Strip all whitespace.
# Try converting to a number.
# If it fails just hmmm...