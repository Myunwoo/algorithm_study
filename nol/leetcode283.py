class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                cur = i
                target = i - 1
                while target > -1:
                    if nums[target] != 0:
                        break
                    nums[cur], nums[target] = nums[target], nums[cur]
                    cur -= 1
                    target -= 1
        