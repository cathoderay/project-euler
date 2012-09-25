#
# File: 9.py
# Description: http://projecteuler.net/problem=9
#

SUM=1000

print reduce(lambda x, y: x*y, 
             [(i, j - i, SUM - j) 
              for i in range(1, SUM) 
              for j in range(i + 1, SUM) 
              if ((SUM - j)**2 == i**2 + (j - i)**2)][0])
