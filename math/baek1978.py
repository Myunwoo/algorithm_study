from math import sqrt

N = int(input())
nums = list(map(int, input().split()))
count = 0
def is_primenum(x):
  if x < 2:
    return False
  for i in range(2, int(sqrt(x) + 1)):
    if x % i == 0:
        return False
  return True

for num in nums:
  if is_primenum(num):
    count += 1

print(count)