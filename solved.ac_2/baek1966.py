import heapq

N = int(input())
for _ in range(N):
  N, M = list(map(int, input().split()))
  costArr = list(map(int, input().split()))
  sortedArr = sorted(costArr)
  
