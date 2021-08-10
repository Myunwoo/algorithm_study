#https://www.acmicpc.net/problem/1715
import sys
import heapq
N=int(sys.stdin.readline())
cards=[]
for _ in range(N):
    cards.append(int(sys.stdin.readline()))

heapq.heapify(cards)
result=0
while True:
    if len(cards)==1:
        break
    first=heapq.heappop(cards)
    second=heapq.heappop(cards)
    result+=first+second
    heapq.heappush(cards,first+second)

print(result)