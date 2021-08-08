#https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = 0
    #여벌 가지고 왔지만 도둑맞은 경우
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)
    
    for r in reserve:
        if (r-1) in lost:
            lost.remove(r-1)
        elif(r+1) in lost:
            lost.remove(r+1)
    answer=n-len(lost)
        
    return answer