#
# File: 1.py
# Description: http://projecteuler.net/problem=1
#

print sum([x for x in range(1000) if not (x % 5 and x % 3)])
