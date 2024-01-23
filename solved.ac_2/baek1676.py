N = int(input())
count = 0
num = 1
for i in range(1, N+1):
  num *= i
num = str(num)

for i in range(len(num)-1, -1, -1):
  if num[i] != '0':
    break
  else:
    count += 1

print(count)