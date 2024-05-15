import sys
input = sys.stdin.readline

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