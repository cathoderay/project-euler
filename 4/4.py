#
# File: 4.py
# Description: http://projecteuler.net/problem=4
#


def is_palindrome(n):
    n = str(n)
    while len(n) > 0 and n[0] == n[-1]:
        n = n[1:-1]
    return len(n) == 0


print max([i*j for i in range(999, 900, -1) 
               for j in range(i, 900, -1)
               if is_palindrome(i*j)])

