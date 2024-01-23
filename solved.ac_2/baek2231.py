N = int(input())
answer = 0

for num in range(N):
  s = num
  num = str(num)
  for n in num:
    s += int(n)
  if s == N:
    answer = num
    break

print(answer)