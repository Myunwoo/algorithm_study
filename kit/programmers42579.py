import heapq

def solution(genres, plays):
    answer = []
    gHashMap = {}
    mHashMap = {}
    
    for i in range(len(genres)):
        # 장르
        if genres[i] in gHashMap:
            gHashMap[genres[i]] += plays[i]
        else:
            gHashMap[genres[i]] = plays[i]
        
        # 음악
        if genres[i] in mHashMap:
            heapq.heappush(mHashMap[genres[i]], (-plays[i], i))
        else:
            mHashMap[genres[i]] = [(-plays[i], i)]
    
    arr = []
    for g in gHashMap:
        arr.append([gHashMap[g], g])
    arr.sort(reverse=True)
    
    for a in arr:
        val, typ = a
        for i in range(2):
            if mHashMap[typ]:
                answer.append(heapq.heappop(mHashMap[typ])[1])
    
    return answer