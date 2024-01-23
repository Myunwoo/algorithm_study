N = int(input())
num = 666
answer = 0

while True:
  if '666' in str(num):
    answer += 1
  if answer == N:
    break
  num += 1

print(num)