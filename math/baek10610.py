#https://www.acmicpc.net/problem/10610
N=list(input())
N.sort(reverse=True)
s=0
for n in N:
    s+=int(n)

if (s%3)!=0 or not N.__contains__('0'):
    print(-1)
else:
    print(''.join(N))