# -----------------------------------------------------------------------------
# locate_list_Element.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module locates the position of a header in a list.
# It provides the information to the user.

# -----------------------------------------------------------------------------
# FUNCTIONS
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
# MAIN
if __name__ == "__main__":
    # Define a test list.
    List = [["#Poop", "Yummy!"], ["##Anna", 21.5], ["#SPECTRUM", \
            "0.5"], ["1.111"], ["64", "0.335"], ["#END", "Test"]]

    for i in list: print(i)
    
    # Call the function.
    Header_info = Locate_list_element(List, "##Anna")
    
    # Print results.
    print(Header_info)