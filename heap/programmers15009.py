import heapq

def solution(ability, number):
    heapq.heapify(ability)
    for _ in range(number):
        s = heapq.heappop(ability) + heapq.heappop(ability)
        heapq.heappush(ability, s)
        heapq.heappush(ability, s)
    return sum(ability)