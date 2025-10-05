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


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0

        while idx < len(nums) - 1:
            if nums[idx] != 101 and nums[idx] == nums[idx+1]:
                curIdx = idx+1
                while curIdx < len(nums) and nums[idx] == nums[curIdx]:
                    nums[curIdx] = 101
                    curIdx += 1
            idx += 1
        
        nums.sort()
        l = len(nums)
        for i in range(len(nums)):
            if nums[i] == 101:
                l = i
                break
        
        nums = nums[:l]
        return l
        
