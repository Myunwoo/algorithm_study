#https://www.acmicpc.net/problem/15922
import sys
N=int(sys.stdin.readline())
start=0
end=0
total=0
for i in range(N):
    s,e=map(int, sys.stdin.readline().split())
    if i==0:
        start=s
        end=e
    else:
        #겹쳐져 그려지는 경우
        if s<=end:
            #선분이 늘어나는 경우
            if e>=end:
                end=e
        #겹쳐지지 않은 경우
        else:
            total+=end-start
            end=e
            start=s
            
print(total+end-start)