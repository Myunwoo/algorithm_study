from itertools import permutations

N, M = map(int, input().split())
nums = list(input().split())

result = list(set(list(permutations(nums, M))))
result.sort()

for r in result:
    print(' '.join(r))