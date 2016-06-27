from sys import stdin
from operator import mul


n = str(stdin.readline())

print max([reduce(mul, map(int, n[i:i+13]))
           for i in range(0, 987)])
