import sys

def solution(stones, k):
    left=1
    right=200000000
    
    while left<=right:
        mid=(left+right)//2
        count=0
        #mid명이 돌다리를 건널 수 있을까?
        for s in stones:
            #mid명이 건너면 돌다리가 부서짐
            if s-mid<=0:
                count+=1
            #연속되어 부서지는 경우가 중요하기 때문에 안부서지면 count를 0으로 초기화
            else:
                count=0
            #부서지는 돌다리의 개수가 k개가 되었음
            if count==k:
                break
                
        if count>=k:
            right=mid-1
        else:
            left=mid+1
    
    return left