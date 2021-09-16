#https://www.acmicpc.net/problem/10162
T=int(input())
a,b,c=300,60,10

ta=T//a
T%=a
tb=T//b
T%=b
tc=T//c
T%=c

if T==0:
    print(str(ta)+' '+str(tb)+' '+str(tc))
else:
    print(-1)