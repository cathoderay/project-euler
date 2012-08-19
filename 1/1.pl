# File: 1.pl
# Description: http://projecteuler.net/problem=1

print eval join '+', grep { !($_ % 3) || !($_ % 5) } (3..999);
