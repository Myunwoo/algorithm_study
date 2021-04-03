n = input()

nums = list(n)

for num in nums:
    num = int(num)

nums.sort(reverse=True)

for num in nums:
    print(str(num),end='')