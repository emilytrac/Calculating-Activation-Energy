from scipy.stats import linregress
import numpy as np


def errors(x, MSD):
    '''
    The error in Ds values obtained from MSD plots
    
    Args:
        x (array) = The time values for the MD simulation
        MSD (array) = The MSD values obtained in an MD simulation
        
    Out:
        Errors (array) = The error in the Ds values obatined from MSD data
    '''
    error_values = []
    
    for i in MSD:
        
        first = linregress(x[0:166], i[0:166])
        second = linregress(x[167:333], i[167:333])
        third = linregress(x[334:499], i[334:499])

        Ds = [first.slope / 6, second.slope / 6, third.slope / 6]

        error = np.var(Ds)
        
        error_values.append(error * 1e-8)
    
    return error_values
