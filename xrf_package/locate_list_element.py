# -----------------------------------------------------------------------------
# locate_list_element.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module locates the position of a header in a list.
# It provides the information to the user.

# -----------------------------------------------------------------------------
# FUNCTIONS
def locate_list_element(list, element):
# Search the list for the specified element. Once found it will be returned to
# the user.
# WARNING! This module's "element" input is case sensitive.

    try:
    
        position = [val[-1] for i, val in enumerate(list) if val[0] == element]
        
        return position[0]
    
    except:
    
        print("ERROR: Element not found. Check input is exact.")

# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    # Define a test list.
    list = [["#Poop", "Yummy!"], ["##Anna", 21.5], ["#SPECTRUM", \
            "0.5"], ["1.111"], ["64", "0.335"], ["#END", "Test"]]

    for i in list: print(i)
    
    # Call the function.
    header_info = locate_list_element(list, "##Anna")
    
    # Print results.
    print(header_info)