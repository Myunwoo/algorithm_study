import sys
input = sys.stdin.readline

n = int(input())
arr = []
def myRound(num):
  return int(num) + (1 if num - int(num) >= 0.5 else 0)

def solution(n, arr):
  if n == 0:
    print(0)
    return
  arr = [int(input()) for _ in range(n)]
  arr.sort()
  num = myRound(n*0.15)
  
  arr = arr[num:n-num]

  # arr = arr[num:len(arr)-num]
  print(myRound(sum(arr)/len(arr)))

solution(n, arr)