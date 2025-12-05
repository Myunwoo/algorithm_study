class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]

            if midVal == target:
                return mid
            elif midVal < target:
                left = mid + 1
            elif midVal > target:
                right = mid - 1
        
        return right if right > left else left
        