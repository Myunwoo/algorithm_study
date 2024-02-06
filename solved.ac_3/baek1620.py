import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
dicNum = {}
dicName = {}
answer = []
for i in range(N):
  name = input()
  dicNum[i+1] = name
  dicName[name] = i+1
for j in range(M):
  inputStr = input()

  findByName = True
  for s in inputStr:
    if not s.isalpha():
      findByName = False
  
  if findByName:
    answer.append(dicName[i])
  else:
    answer.append(dicNum[int(i)])
    
for a in answer:
  print(a)