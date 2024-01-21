import math

A, B, V = list(map(int, input().split()))
V -= A
print(math.ceil(V/(A-B)) + 1)
