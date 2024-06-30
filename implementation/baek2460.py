stack = [list(map(int, input().split())) for _ in range(10)]

answer = -1
cur = 0
for s in stack:
  cur = cur + s[1] - s[0]
  answer = max(answer, cur)

print(answer)