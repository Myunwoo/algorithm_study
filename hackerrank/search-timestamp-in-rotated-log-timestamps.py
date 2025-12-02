def searchRotatedTimestamps(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        midVal = nums[mid]
        
        if midVal == target:
            return mid
        
        if nums[left] <= midVal:
            if nums[left] <= target < midVal:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if midVal < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# 회전된 정렬 배열에서 이분 탐색
# 주목해야 하는 성질은 mid 기준으로 항상 한 쪽은 정렬 상태라는 점이다.
# mid를 기준으로 정렬된 쪽이 어느 쪽인지를 판단하고, 정렬된 쪽에 target이 속한다면 해당 범위 내에서 이분 탐색을 이어가도록 처리하면 되고,
# 정렬된 쪽에 target이 속하지 않는다면 반대쪽으로 동일 로직을 시작하면 됨.