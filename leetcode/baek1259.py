import sys

while True:
    num = sys.stdin.readline().strip()

    if num == '0':
        break

    if num[len(num)-1] == '0':
        print('no')
        continue

    isPellindrome = True
    for i in range(len(num) // 2):
        if num[i] != num[len(num)-i-1]:
            isPellindrome = False
            break

    if isPellindrome:
        print('yes')
    else:
        print('no')


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