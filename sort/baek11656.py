#https://www.acmicpc.net/problem/11656
S=list(input())
S.reverse()
arr=[]
for i in range(len(S)):
    temp=''
    for j in range(i,-1,-1):
        temp+=S[j]
    arr.append(temp)

arr.sort()
for a in arr:
    print(a)