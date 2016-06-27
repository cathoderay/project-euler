from sys import stdin


n = str(stdin.readline())

print max([reduce(lambda x, y: int(x)*int(y), n[i:i+13])
           for i in range(0, 987)])
