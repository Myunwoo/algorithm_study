from itertools import combinations
nums = [int(input()) for _ in range(9)]
for col in combinations(nums, 7):
  if sum(col) == 100:
    for c in sorted(col):
      print(c)
    break