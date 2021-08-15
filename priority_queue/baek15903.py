#https://www.acmicpc.net/problem/15903
import heapq

N,M=map(int, input().split())
cards=list(map(int, input().split()))

heapq.heapify(cards)
for _ in range(M):
    x=heapq.heappop(cards)
    y=heapq.heappop(cards)
    heapq.heappush(cards,x+y)
    heapq.heappush(cards,x+y)

print(sum(cards))