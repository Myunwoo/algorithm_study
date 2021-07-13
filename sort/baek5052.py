#https://www.acmicpc.net/problem/5052
import sys

results = []

t=int(sys.stdin.readline().strip())
for l in range(t):
    n = int(sys.stdin.readline().strip())
    numbers = [sys.stdin.readline().strip() for _ in range(n)]
    numbers.sort()
    results.append("YES")
    for i in range(len(numbers)-1):
        if numbers[i+1].startswith(numbers[i]):
            results[l]="NO"
            break

for r in results:
    print(r)