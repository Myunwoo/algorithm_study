#https://www.acmicpc.net/problem/2470

N = int(input())
cups = list(map(int, input().split()))
cups.sort()

left = 0
right = N-1

m = cups[left] + cups[right]
result = [m, cups[left], cups[right]]

while left < right:
    s = cups[left] + cups[right]
    if s == 0:
        result = [s,cups[left],cups[right]]
        break
    if abs(s) < abs(result[0]):
        result = [s,cups[left],cups[right]]
    elif s < 0:
        left+=1
    elif s > 0:
        right -= 1

print(str(result[1]) + ' ' + str(result[2]))