nums = []
while True:
    num = input()
    if num == '0':
        break
    nums.append(num)

for num in nums:
    r = ''.join(list(reversed(num)))
    if r == num:
        print('yes')
    else:
        print('no')