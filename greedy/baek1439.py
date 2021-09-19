#https://www.acmicpc.net/problem/1439
S=list(input())
flag='2'
c0=0
c1=0
for s in S:
    if s!=flag:
        if s=='0':
            c0+=1
        elif s=='1':
            c1+=1
        flag=s

print(min(c0,c1))   