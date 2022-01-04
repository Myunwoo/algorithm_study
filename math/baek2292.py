#https://www.acmicpc.net/problem/2292
N=int(input())
num=1
i=1
while True:
    num+=6*(i-1)
    if num>=N:
       break
    i+=1

print(i)
