# File: 1.rb
# Description: http://projecteuler.net/problem=1

p (3...1000).select{|x| x % 3 == 0 || x % 5 == 0}.inject{|x, y| x + y}
