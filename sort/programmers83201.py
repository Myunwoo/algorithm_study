#https://programmers.co.kr/learn/courses/30/lessons/83201
import sys
def solution(scores):
    answer = ''
    N=len(scores[0])
    for i in range(N):
        temp=[]
        mine=0
        for j in range(N):
            if i==j:
                mine=scores[j][i]
            temp.append(scores[j][i])
        temp.sort()
        if mine==max(temp) and temp[N-1]!=temp[N-2]:
            temp.remove(mine)
        elif mine==min(temp) and temp[0]!=temp[1]:
            temp.remove(mine)
        avg=sum(temp)/len(temp)
        if avg>=90:
            answer+='A'
        elif avg>=80:
            answer+='B'
        elif avg>=70:
            answer+='C'
        elif avg>=50:
            answer+='D'
        else:
            answer+='F'
    return answer