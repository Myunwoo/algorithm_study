import math

n = int(input())
arr = []

def solution(n, arr):
  for _ in range(n):
    arr.append(int(input()))
  arr.sort()

  l = len(arr)
  num = math.ceil(l*0.15)
  if num*2 >= l:
    print(0)
    return

  arr = arr[num+1:len(arr)-num]
  print(math.ceil(sum(arr)/len(arr)))

solution(n, arr)