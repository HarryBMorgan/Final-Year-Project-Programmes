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

    Fluorescence_dict = {"Br wk": 0.618, "Br w1": 3.6e-3, "Br w2": 0.018, \
                    "Br w3": 0.020, "Pb wk": 0.967, "Pb w1": 0.112, \
                    "Pb w2": 0.373, "Pb w3": 0.360, "Pb wm": 0.0292, \
                    "Cl wk": 0.097, "Cl w1": 1.2e-4, "Cl w2": 2.4e-4, \
                    "Cl w3": 2.4e-4, "Cs wk": 0.897, "Cs w1": 0.049, \
                    "Cs w2": 0.090, "Cs w3": 0.091}
    
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