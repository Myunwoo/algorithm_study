import sys

N = int(input())

times = list(map(int, input().split()))

times.sort()

result = 0

for i in range(len(times)):
    for j in range(i+1):
        result += times[j]

print(result)