# Individual Homework 1 for Alan Gale

## Part 1: Estimating Pi
Estimate $\int_{0}^{1}$ $\frac{1}{1 + x^2}$ dx using a Monte Carlo simulation. <br> Note that this result can be found in closed form by trigonometric substitution which will be used to evaluate the accuracy of our result. <br> 

Using x = $\tan\theta$, ${dx = sec^2\theta  d\theta}$, and ${1 + x^2}$ = ${1 + tan^2\theta}$ = ${sec^2\theta}$. At x = 0, $\theta$ = 0. <br> At x = 1, $\theta = \frac{\pi}{4}$. <br> Rewriting the integral, $\int_{0}^{1}$ $\frac{1}{1 + x^2}$ dx = $\int_{0}^{\frac{\pi}{4}}$ $\frac{\sec^2}{\sec^2}$ $d\theta$ = $\int_{0}^{\frac{\pi}{4}}$ $d\theta$ = $\frac{\pi}{4}$. The value of ${\pi}$ can then be estimated by multipying our result by 4.<br> 

First, I determined the range of values for y given the range of values for x. At x = 0, y = 1. At x = 1, y = 1/2. Thus the boundaries for our random values are x from [0, 1], and y from [0, 1]. <br> 
Second, I generated random values of (x, y) coordinates over their respective ranges, and estimate the area under the curve $\frac{1}{1 + x^2}$ by the ratio of the number of y values less than $\frac{1}{1 + x^2}$ divided by total number of generated (x, y) value pairs, then multiplying by 4 to obtain the estimate of ${\pi}$.


## Part 2: Estimating Second Integrand
Estimate $\int_{0}^{1}$ $\frac{10}{1 + 100x^2}$ dx using a Monte Carlo simulation. <br> Note that this result can be found in closed form by trigonometric substitution which will be used to evaluate the accuracy of our result. <br> 
Using x = \frac($\tan\theta$}{10}, ${dx = \frac{sec^2\theta}{10}  d\theta}$, and ${1 + 100x^2}$ = ${1 + tan^2\theta}$ = ${sec^2\theta}$. At x = 0, $\theta$ = 0. <br> At x = 1, $\theta$ = $\operatorname{atan}(10)$ = ~1.4711. <br> Rewriting the integral, $\int_{0}^{1}$ $\frac{10}{1 + 100x^2}$ dx = $\int_{0}^{1.47}$ $\frac{10\sec^2}{\sec^2}$ $10d\theta$ = $\int_{0}^{1.47}$ $d\theta$ ~= 1.4711. 

First, I determined the range of values for y given the range of values for x. At x = 0, y = 10. At x = 1, y = 10/101. Thus the boundaries for our random values are x from [0, 1], and y from [0, 10], except from experimentation, my results did not converge to the known value with this high peak. Instead I ran the same intgral with 1 in the numerator instead of 10, and then multiplied the estimate by 10 to produce the final result. <br> 
Second, I generated random values of (x, y) coordinates over their respective ranges, and estimated the area under the curve $\frac{1}{1 + 100x^2}$ by the ratio of the number of y values less than $\frac{1}{1 + 100x^2}$ divided by total number of generated (x, y) value pairs, then muliplied the final result by 10. This proved far more effective, producing a very close result to the known value.

## The repository contents contain the following files:
gale_alan_individual_homework1.ipynb
gale_alan_individual_homework1.py
gale_alan_README_individual_homework1.md (this file)

## How to run the script. 
Execute the gale_alan_individual_homework1.py using the Jupyter notebook gale_alan_individual_homework1.ipynb. This will import and call the functions in the gale_alan_individual_homework1.py file.

## Test Cases
For each of the two functions incorporated testing functions as they were built by creating short, manageable arrays emulating the random x_values, random y_values, deterministic y_threshold values (using the functions and the known x_values), boolean comparisons between random y_values and y_threshold values, and the count of valid comparisons where random y_values were less than deterministic y_threshold values. In addition the following assert statements were implemented to test the code in each task:
1. Verified all random x_values were greater than 0.0 and less than 1.0;
2. Verified all random y_values were greater than 0.0 and less than 1.0;
3. Verified all counts when y_values < y_threshold values did not exceed the number of point and was greater than zero;
4. Verified the final results were within 10% of the known or calculated values of the integrals.

This last test was the most important to verify the methodology, and was the chief failure point in the initial runs of Task 2 (estimate_second_integral) revealing that the results were far off the known values. This test in particular led me to change the the function to use 1 in the numerator instead of 10, to change the y_max value to 1.0 instead of 10, and then scaling the final estimate by the factor of 10.
