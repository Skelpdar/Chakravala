# Chakravala
Given a positive integer N, the method solves Pell's equation on the form x^2-N*y^2=1 for positive integers x and y. The solution will give the smallest such x. 
If N is a square, there is no solution where y > 0. Lagrange showed that this method always terminates in a solution. 

This is done using the chakravala method, also known as the cyclic method, which is attributed to the 12th century mathematician Bhāskara II. See https://en.wikipedia.org/wiki/Chakravala_method  

## Usage
The method chakravala(N):

*Arguments*: N, a positive integer

*Returns*: (x, y), positive integers x and y which solves the equation. 
