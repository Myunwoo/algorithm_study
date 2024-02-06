nums = input().split('-')

answer = 0
first = nums[0]
if '+' in first:
  first = first.split('+')
  for i in range(len(first)):
    first[i] = int(first[i])
  answer = sum(first)
else:
  answer = int(first)

for i in range(1, len(nums)):
  s = 0
  if '+' in nums[i]:
    arr = nums[i].split('+')
    for j in range(len(arr)):
      arr[j] = int(arr[j])
    s = sum(arr)
  else:
    s = int(nums[i])
  answer -= s
print(answer)