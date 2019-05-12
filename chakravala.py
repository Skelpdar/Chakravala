import math
from fractions import Fraction



"""
For a solution a**2-N*b**2=k, return a new such tuple. 
"""
def selfcomposition(a,b,k,N):
    
    #Find the positive integer m such that k divides (a+b*m)
    #and abs(m**2-N) is minimized. 
    mguess = 1
    m = 1

    #The numerator of k, m**2-N, that is to be minimized
    knum = 0
    while True:
        if ((a+b*mguess)/k) % 1 == 0:
            if knum == 0:
                 knum = abs(mguess**2-N)
                 m = mguess
            elif abs(mguess**2-N) < knum:
                knum = abs(mguess**2-N)
                m = mguess
            else:
                break
        mguess += 1

    #Redefine the tuple (a,b,k) with a new solution
    solution = ((a*m+N*b)/abs(k),(a+m*b)/abs(k), (m**2-N)/k)

    return solution



"""
Uses the Chakravala cyclic method to solve, given a positive integer N, 
for the positive integers x and y, which solves x**2-N*y**2=1 where x is minimized.
If N is a square, there is no solution with y > 0. 
"""
def chakravala(N):
    #Guess an initial tuple (a,b,k)
    #where a**2-N*b**2=k
    a = Fraction(14)
    b = Fraction(1)
    k = a**2-N*b**2

    #Use self composition until k = 1
    #This will terminate for N which are not squares 
    while True:
        #Find a new solution
        a,b,k = selfcomposition(a,b,k,N)

        #Terminate if correct
        if k == 1:
            break

    return (int(a),int(b))
