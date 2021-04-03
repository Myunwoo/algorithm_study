import sys

n = int(sys.stdin.readline())

points = []
a=0
b=0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    points.append((a,b))

points.sort(key=lambda x:(x[0],x[1]))

for point in points:
    print(str(point[0]) + ' ' + str(point[1]))