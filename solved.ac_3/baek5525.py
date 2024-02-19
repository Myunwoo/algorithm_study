N = int(input())
M = int(input())
S = input()

answer = 0
stack = []
for i in range(len(S)):
  if S[i] == 'I' and not stack:
    stack.append(S[i])
    continue
  elif S[i] == 'O' and not stack:
    continue
  
  if stack[-1] != S[i]:
    stack.append(S[i])
    if len(stack) == 2*N+1:
      answer += 1
      stack.pop()
      stack.pop()
  else:
    if S[i] == 'I':
      stack = ['I']
    else:
      stack = []

print(answer)