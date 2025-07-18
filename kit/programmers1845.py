def solution(nums):
    max_select = len(nums) // 2
    unique_types = len(set(nums))
    return min(max_select, unique_types)
