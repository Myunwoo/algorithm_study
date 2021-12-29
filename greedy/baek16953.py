#https://www.acmicpc.net/problem/16953
A,B=map(int,input().split())
count=0

while True:
    if A>=B:
        break
    if B%10==1:
        B//=10
    elif B%2==0:
        B//=2
    else:
        break
    count+=1

if A==B:
    print(count+1)
else:
    print(-1)