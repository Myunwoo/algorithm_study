N = int(input())
M = int(input())
wrongs = input().split()
big = ''
small = ''
bigGood = True
smallGood = True

val = 0
while True:
  bigGood = True
  smallGood = True
  cur = N
  big = str(cur + val)
  small = str(cur - val)
  for w in wrongs:
    if w in big:
      bigGood = False
      break
  for w in wrongs:
    if w in small:
      smallGood = False
      break
  
  if bigGood or smallGood:
    break
  val += 1

answer = float('inf')
if bigGood:
  answer = min(len(big)+abs(N-int(big)), abs(N-100))
elif smallGood:
  answer = min(len(big)+abs(N-int(big)), abs(N-100))

print(answer)