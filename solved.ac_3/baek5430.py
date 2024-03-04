import sys
from collections import deque
input = sys.stdin.readline

answer = []

T = int(input())
for _ in range(T):
  p = list(input().strip())
  n = int(input())
  i = input().strip()
  i=i.replace('[','')
  i=i.replace(']','')
  arr = list(i.split(','))
  dq = deque()
  isError = False
  for a in arr:
    if a.isnumeric():
      dq.append(a)
  
  front = True
  for pp in p:
    if pp == 'R':
      front = not front
    else:
      if len(dq) < 1:
        answer.append('error')
        isError = True
        break
      if front:
        dq.popleft()
      else:
        dq.pop()

  if isError:
    continue

  if front:
    answer.append(dq)
  else:
    answer.append(list(reversed(dq)))


for a in answer:
  if a == 'error':
    print(a)
  else:
    print('[', end='')
    for i in range(len(a)):
      print(a[i], end='')
      if i < len(a)-1:
        print(',',end='')
    print(']')