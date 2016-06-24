#
# File: 4.py
# Description: http://projecteuler.net/problem=4
#

# Idea: brute force + cutoff threshold (900)

def is_palindrome(n):
    n = str(n)
    while len(n) > 0 and n[0] == n[-1]:
        n = n[1:-1]
    return len(n) == 0


print max([i*j for i in range(900, 1000) 
               for j in range(i, 1000)
               if is_palindrome(i*j)])

