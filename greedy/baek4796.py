#https://www.acmicpc.net/problem/4796
import sys
results=[]
while True:
    L,P,V=map(int, sys.stdin.readline().split())
    if L==0 and P==0 and V==0:
        break
    temp=(V//P)*L
    if (V%P)<=L:
        temp+=V%P
    elif V%P>L:
        temp+=L
    results.append(temp)

for i in range(len(results)):
    print('Case '+str(i+1)+': '+str(results[i]))