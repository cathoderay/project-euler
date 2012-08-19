# File: 1.R
# Description: http://projecteuler.net/problem=1

x <- 3:999
print(sum(x[x %% 3 == 0 | x %% 5 == 0]))
