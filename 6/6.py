#
# File: 6.py
# Description: http://projecteuler.net/problem=6
#

# Idea: Straightforward. Used the fact that 1 + 2 + ... 100 = 5050 (A.P. Sum)
#       Btw, there is a O(1) solution to compute the sum of squares.
#       http://www.trans4mind.com/personal_development/mathematics/series/sumNaturalSquares.htm 


print 5050**2 - sum(map(lambda x: x*x, range(101)))
