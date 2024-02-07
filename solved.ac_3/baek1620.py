import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
dicNum = {}
dicName = {}
answer = []
for i in range(N):
  name = input().rstrip()
  dicNum[i+1] = name
  dicName[name] = i+1
for j in range(M):
  inputStr = input().rstrip()

  if inputStr.isnumeric():
    answer.append(dicNum[int(inputStr)])
  else:
    answer.append(dicName[inputStr])
     
for a in answer:
  print(a)