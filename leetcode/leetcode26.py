class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        count = 1
        left, right = 0, 1

        while right < len(nums):
            if nums[left] == nums[right]:
                nums[right] = 101
                right += 1
            else:
                count += 1
                left = right
                right = left + 1

        nums.sort()
        return count