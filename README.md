# Homework 1 for Alan Gale

## Part 1: Estimating Pi
Estimate $\int_{0}^{1}$ $\frac{1}{1 + x^2}$ dx using a Monte Carlo simulation. <br> Note that this result can be found in closed form by trigonometric substitution which will be used to evaluate the accuracy of our result. <br> 

Using x = $\tan\theta$, ${dx = sec^2\theta  d\theta}$, and ${1 + x^2}$ = ${1 + tan^2\theta}$ = ${sec^2\theta}$. At x = 0, $\theta$ = 0.  At x = 1, $\theta = \frac{\pi}{4}$. <br> Rewriting the integral, $\int_{0}^{1}$ $\frac{1}{1 + x^2}$ dx = $\int_{0}^{\frac{\pi}{4}}$ $\frac{\sec^2}{\sec^2}$ $d\theta$ = $\int_{0}^{\frac{\pi}{4}}$ $d\theta$ = $\frac{\pi}{4}$ - 0 = $\frac{\pi}{4}$. The value of ${\pi}$ can then be estimated by multipying our result by 4.<br> 

First, I determined the range of values for y given the range of values for x. At x = 0, y = 1. At x = 1, y = 1/2. Thus the boundaries for our random values are x from [0, 1], and y from [0, 1]. <br> 
Second, I generated random values of (x, y) coordinates over their respective ranges, and estimate the area under the curve $\frac{1}{1 + x^2}$ by the ratio of the number of y values less than $\frac{1}{1 + x^2}$ divided by total number of generated (x, y) value pairs, then multiplying by 4 to obtain the estimate of ${\pi}$.


## Part 2: Estimating Second Integrand
Estimate $\int_{0}^{1}$ $\frac{10}{1 + 100x^2}$ dx using a Monte Carlo simulation. <br> Note that this result can be found in closed form by trigonometric substitution which will be used to evaluate the accuracy of our result. <br> 
Using x = $\frac{\tan(\theta)}{10}$, ${dx = \frac{sec^2\theta}{10}  d\theta}$, yielding ${1 + 100x^2}$ = ${1 + tan^2\theta}$ = ${sec^2\theta}$. <br>At x = 0, $\theta$ = 0. At x = 1, $\theta$ = $\operatorname{atan}(10)$ = ~1.4711. <br> Rewriting the integral, $\int_{0}^{1}$ $\frac{10}{1 + 100x^2}$ dx = $\int_{0}^{{atan}(10)}$ $\frac{\sec^2}{\sec^2}$ $d\theta$ = $\int_{0}^{{atan}(10)}$ $d\theta$ = ${atan}(10)$ - 0 = ${atan}(10)$ ~= 1.4711. 

First, I determined the range of values for y given the range of values for x. At x = 0, y = 10. At x = 1, y = 10/101. Thus the boundaries for our random values are x from [0, 1], and y from [0, 10]. <br> 
Second, I generated random values of (x, y) coordinates over their respective ranges, and estimated the area under the curve $\frac{10}{1 + 100x^2}$ by the ratio of the number of y values less than $\frac{10}{1 + 100x^2}$ divided by total number of generated (x, y) value pairs.  Since the test space has an area of x_range * y_range = (1)(10) = 10, I multiplied a test area scale factor of 10 to the preliminary result yielding the final estimate of the area under the curve.

## The repository contents contain the following files:
assignment.ipynb
assignment.py
README.md (this file)

## How to run the script. 
Execute the assignment.py using the Jupyter notebook assignment.ipynb running all the code. This will import and call the functions in the assignment.py file. Results for the number of data points and accuracy is printed out for each task.

## Test Cases
For each of the two functions incorporated testing functions as they were built by creating short, manageable arrays emulating the random x_values, random y_values, deterministic y_threshold values (using the functions and the known x_values), boolean comparisons between random y_values and y_threshold values, and the count of valid comparisons where random y_values were less than deterministic y_threshold values. In addition the following assert statements were implemented to test the code in each task:
1. Verified all random x_values were greater than 0.0 and less than 1.0;
2. Verified all random y_values were greater than 0.0 and less than 1.0;
3. Verified all counts when y_values < y_threshold values did not exceed the number of point and was greater than zero;
4. Verified the final results were within 10% of the known or calculated values of the integrals.

This last test was the most important to verify the methodology, and revealed an initial error in Task 2 by not applying the 10x scale factor based on the test area of 10. Final values were within 1% of known values when 100,000 data points were utilized.