#https://www.acmicpc.net/problem/2920

nums = list(map(int, input().split()))

typeOfNums = 0

if nums[0] == 1:
    typeOfNums = 1
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            typeOfNums = 0
            break
elif nums[0] == 8:
    typeOfNums = 2
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            typeOfNums = 0
            break
else:
    typeOfNums = 0


if typeOfNums == 0:
    print("mixed")
elif typeOfNums == 1:
    print("ascending")
else:
    print("descending")