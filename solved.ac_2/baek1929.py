import math

M, N = list(map(int, input().split()))

arr = [True for _ in range(1000001)]
arr[1] = False

for i in range(2, math.ceil(1000001**0.5)):
  for ii in range(i+i, 1000001, i):
    arr[ii] = False

for i in range(M, N+1):
  if arr[i] == True:
    print(i)