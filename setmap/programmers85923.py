def solution(nums):
    answer = 0
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    answer = min(len(dic), len(nums)//2)
    return answer