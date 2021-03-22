# -----------------------------------------------------------------------------
# fluorescence_yield.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This module locates the correct fluorescence yield and returns it to user.

# -----------------------------------------------------------------------------
# FUNCTIONS
def fluorescence_yield(Element, Yield):
# This function takes the elemental symbol and shell designation (e.g. "Br", 
# "w1") as type str and returns the fluorescence yield for that element at
# that shell.

    Fluorescence_dict = {"Br wk": 0.6275, "Br wl": 0.0195, "Br wm": 3.02e-4, \
                    "Pb wk": 0.9634, "Pb wl": 0.369, "Pb wm": 0.0292, \
                    "Cl wk": 0.09892, "Cl wl": 0.00118, \
                    "Cs wk": 0.8942, "Cs wl": 0.0938, "Cs wm": 0.00401}
    
    # Find which yield we're talking about and return it to the user.
    return Fluorescence_dict[Element + " " + Yield]

# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    # Create input variables.
    Element = "Cl"
    Yield = "w3"
    
    # Call function.
    val = fluorescence_yield(Element, Yield)
    
    # Print value returned from function.
    print(val)