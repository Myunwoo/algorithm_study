#https://www.acmicpc.net/problem/10821
S=list(input())
count=0
for _ in range(len(S)):
    t = S.pop()
    if t==',':
        count+=1

print(count+1)