-- File: 1.hs
-- Description: http://projecteuler.net/problem=1 

sum([x | x <- [3..999], mod x 3 == 0 || mod x 5 == 0])
