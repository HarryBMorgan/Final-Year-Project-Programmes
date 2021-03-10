# -----------------------------------------------------------------------------
# evaluate_peak.py

# -----------------------------------------------------------------------------
# Final Year Project - XRF Analysis
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# This programme integrates and finds the max energy of a spectal peak provided
# by user input.

# -----------------------------------------------------------------------------
# IMPORTS
from numpy import linspace
from scipy.integrate import simps

# -----------------------------------------------------------------------------
# FUNCTIONS
def peak_energy(X_lim, X_data, Y_data):
# This function finds the peak energy for the peak defined by the parameters.
    
    # Create X_lim index.
    a = X_data.index(X_lim[0])
    b = X_data.index(X_lim[-1])
    
    # Find index of max value in Y_data.
    indx = Y_data[a: b].index(max(Y_data[a: b])) + a
    
    # Find associated x_coordinate and return to user.
    return X_data[indx]
 
def integrate_peak(X_lim, X_data, Y_data):
# This function finds the value of the integral below the peak enclosed within
# the boundaries set by the X_lim input. The input N allows for the user to
# decide between speed and accuracy for the integral.

    # Create X_lim index.
    a = X_data.index(X_lim[0])
    b = X_data.index(X_lim[-1])

    # Remove baseline from Y_data.
    Y_data_lowered = __remove_baseline__(a, b, X_data, Y_data)
    
    # Integrate using Simpsons Rule from SciPy.
    count = simps(Y_data_lowered)
    
    # Return the integrated value to the user.
    return count

def __remove_baseline__(a, b, X_data, Y_data):
# This function generates a baseline reading of a straight line between the
# upper and lower x limits and subtracts it from the Y_data.
    
    # Create background seperation line.
    baseline = linspace(Y_data[a], Y_data[b], len(Y_data[a: b+1]))
    
    # Correct Y_data by removing baseline and return to user.
    return Y_data[a: b+1] - baseline

# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    pass