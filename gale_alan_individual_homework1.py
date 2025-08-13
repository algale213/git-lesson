# Individual Homework Assignment 1 by Alan Gale
 
# Part 1: estimating Pi
# Part 2: estimating a second integral  

#Import libraries use by both parts
import math
import numpy as np


#Part 1: estimating Pi

#Initialize variables
np.random.seed(1)          #Create random seed

def estimate_pi(num_points):
    """
    Estimate pi using Monte Carlo simulation of the integral from 0 to 1 of 1/(1 + x^2) dx.

    Parameters
    ----------
    num_points: int
        The number of points used in the simulation.

    Returns
    -------
    pi_estimate: float
        Estimate of pi.
    """   

    #Define range of x and y random values based on integration limits of x, and y = f(x)
    x_values = np.random.uniform(0, 1, num_points)     #Generate a numpy array of random values for x coordinates
    y_values = np.random.uniform(0, 1, num_points)     #Generate a numpy array of random values for y coordinates
    
    #print(f"The x values are {x_values}")     #For troubleshooting
    #print(f"The y values are {y_values}")     #For troubleshooting

    #Compare y_values against y_threshold = f(x_values)
    y_threshold = 1 / (1 + np.power(x_values, 2)) # The values of y according to the function
    y_comparison = y_values < y_threshold
    #print(f"The y threshold values for the given x_values are {y_threshold}")
    #print(f"The comparison of y_values to y_threshold values for the given x_values are {y_comparison}")


    count = np.sum(y_comparison)
    #print(f"The count of y_values under y_threshold is {count}") # For troubleshooting

    #Test with some assert statements
    assert np.all(x_values <= 1.0) and np.all(x_values >= 0.0)
    assert np.all(y_values <= 1.0) and np.all(y_values >= 0.0)
    assert np.all(count <= num_points) and np.all(count >= 0.0)

    #Calculate estimate
    pi_estimate = (count/num_points) * 4

    #Test result is within 10% of truth
    assert math.isclose(pi_estimate, math.acos(-1), abs_tol = math.acos(-1)/10) 


    return pi_estimate


#Part 2: estimating the second integral

def estimate_second_integral(num_points):
    """
    Estimate the second integral using Monte Carlo simulation of the integral from 0 to 1 of 10/(1 + 100*x^2) dx.

    Parameters
    ----------
    num_points: int
        The number of points used in the simulation.

    Returns
    -------
    integral_estimate: float
        Estimate of the integral.
    """   

    #Define range of x and y random values based on integration limits of x, and y = f(x)
    #When x = 0, y = 10. When x = 1, y = 0.099. so use a range of x from [0, 1.0] and normally y from [0, 10.0] but from experimentation with a high peak, we instead
    #ran y from [0.0, 1.0] and then multiplied the final result by 10.
    x_values = np.random.uniform(0, 1, num_points)        #Generate a numpy array of random values for x coordinates
    y_values = np.random.uniform(0, 1.0, num_points)     #Generate a numpy array of random values for y coordinates


    #Compare y_values against y_threshold = f(x_values)
    y_threshold = 1 / (1 + 100 * np.power(x_values, 2)) # The values of y according to the function
    y_comparison = y_values < y_threshold

    count = np.sum(y_comparison)
    
    #Test with some assert statements
    assert np.all(x_values <= 1.0) and np.all(x_values >= 0.0)
    assert np.all(y_values <= 1.0) and np.all(y_values >= 0.0)
    assert np.all(count <= num_points) and np.all(count >= 0.0)

    #Calculate estimate
    integral_estimate = 10 * (count/num_points) # Multipy up the final result by 10 to account for the change in y range and y_threshold values described earlier

    #Test result is within 10% of truth
    #assert math.isclose(integral_estimate, 1.4711, abs_tol = 0.14711) 
    assert math.isclose(integral_estimate, math.atan(10), abs_tol = math.atan(10) / 10) 

    return integral_estimate


