#https://www.acmicpc.net/problem/12904
S=list(input())
T=list(input())

while True:
    l=len(T)
    if l==len(S):
        break
    if T[l-1]=='A':
        T.pop()
    elif T[l-1]=='B':
        T.pop()
        T.reverse()
    


if S==T:
    print(1)
else:
    print(0)