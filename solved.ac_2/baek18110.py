import sys
input = sys.stdin.readline

# 파이썬 반올림은 앞자리 숫자가 홀수면 올림, 짝수면 내림을 하는 특성이 있다.
def myRound(num):
  return int(num) + (1 if num - int(num) >= 0.5 else 0)

answer = 0
n = int(input())
scores = [int(input()) for _ in range(n)]
scores.sort()

div = myRound(n*0.15)
scores = scores[div:len(scores)-div]

if len(scores) > 0:
  answer = myRound(sum(scores)/len(scores))
print(answer)