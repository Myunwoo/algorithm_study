import sys
N, r, c = list(map(int, sys.stdin.readline().split()))
temp = (2**(N-1))*(r//2)*4 + 4*(c//2)
if r%2 == 0 and c%2 == 0:
    temp += 0
elif r%2 == 0 and c%2 == 1:
    temp += 1
elif r%2 ==1 and c%2 == 0:
    temp += 2
else:
    temp += 3
print(temp)