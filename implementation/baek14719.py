#https://www.acmicpc.net/problem/14719
import sys
H,W=map(int, sys.stdin.readline().split())
blocks=list(map(int, sys.stdin.readline().strip().split()))

result = 0

for i in range(1, len(blocks)-1):
    target = min(max(blocks[:i]), max(blocks[i+1:]))
    result += target-blocks[i] if target > blocks[i] else 0

print(result)