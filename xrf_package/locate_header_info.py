# -----------------------------------------------------------------------------
# locate_header_info.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module locates the position of a header in a list.
# It provides the information to the user.

# -----------------------------------------------------------------------------
# FUNCTIONS
def locate_header_info(list, element):
# Search the list for the specified element. Once found it will be returned to
# the user.
# WARNING! This module's "element" input is case sensitive.

    try:
    
        # Begin looping through list to locate 
        for i in range(len(list)):
        
            if element in list[i][0]:
                
                loc_info = list[i]
                break
        
        return loc_info

    except:
    
        return "ERROR: No match found for element."

# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    # Define a test list.
    list = [["#Poop", "Yummy!"], ["##Anna", 21.5], ["#SPECTRUM", \
            "0.5"], ["1.111"], ["64", "0.335"], ["#END", "Test"]]
    
    # Call the function.
    loc_info = locate_header_info(list, "Poop")
    
    # Print results.
    print(loc_info)