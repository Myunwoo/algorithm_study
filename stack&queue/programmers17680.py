#https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache=deque()
    
    for city in cities:
        city=city.lower()
        #캐시 히트
        if city in cache:
            answer+=1
            cache.remove(city)
            cache.appendleft(city)
        #캐시 미스
        else:
            answer+=5
            cache.appendleft(city)
            if len(cache)>cacheSize:
                cache.pop()
    
    return answer