#https://www.acmicpc.net/problem/2831
import sys
N=int(sys.stdin.readline())
men=list(map(int, sys.stdin.readline().strip().split()))
women=list(map(int, sys.stdin.readline().strip().split()))

posM=[]
negM=[]
posW=[]
negW=[]
for i in range(N):
    if men[i] < 0:
        negM.append(men[i])
    else:
        posM.append(men[i])
    if women[i] < 0:
        negW.append(women[i])
    else:
        posW.append(women[i])

posM.sort()
negW.sort(reverse=True)
posW.sort()
negM.sort(reverse=True)


#####안된거
#키 큰 여자와 춤을 추려는 그룹
count=0
for p in posM:
    for n in negW:
        if p+n<0:
            count+=1
            break

#키 작은 여자와 춤을 추려는 그룹
for p in posW:
    for n in negM:
        if p+n<0:
            count+=1
            break

#####된거
count=0
def calForResult(plus, minus):
    i,j = 0,0
    cnt = 0
    while i < len(plus):
        while j < len(minus):
            if plus[i] + minus[j] < 0 :
                j += 1
                cnt += 1
                break
            else :
                j += 1
        if j == len(minus) :
            break
        i += 1
    return cnt

count+=calForResult(posM,negW)
count+=calForResult(posW,negM)
print(count)