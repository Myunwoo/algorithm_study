N, M = list(map(int, input().split()))
a = [input() for _ in range(N)]
b = [input() for _ in range(M)]

dic = {}
for aa in a:
  dic[aa] = 1
for bb in b:
  if bb in dic:
    dic[bb] += 1

answer = []
for key in dic:
  if dic[key] == 2:
    answer.append(key)

answer.sort()
print(len(answer))
for i in answer:
  print(i)