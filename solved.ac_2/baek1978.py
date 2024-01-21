import math

N = int(input())
nums = list(map(int, input().split()))
arr = [True for _ in range(1001)]
arr[1] = False

for i in range(2, math.ceil(1001**0.5)):
  for ii in range(i+i, 1001, i):
    arr[ii] = False

answer = 0
for num in nums:
  if arr[num] == True:
    answer += 1
print(answer)