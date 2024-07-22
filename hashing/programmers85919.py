import heapq

def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        gen = genres[i]
        play = plays[i]
        if gen not in dic:
            dic[gen] = [-play, [[-play, i]]]
        else:
            dic[gen][0] -= play
            heapq.heappush(dic[gen][1], [-play, i])
    arr = []
    for d in dic:
        arr.append(dic[d]+[d])
    heapq.heapify(arr)
    
    while arr:
        c, heap, name = heapq.heappop(arr)
        if len(heap) == 1:
            answer.append(heapq.heappop(heap)[1])
        else:
            answer.append(heapq.heappop(heap)[1])
            answer.append(heapq.heappop(heap)[1])
        
    return answer