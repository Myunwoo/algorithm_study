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
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] != 0:
                found = False
                for j in range(i-1, -1, -1):
                    if nums[j] != 0:
                        found = True
                        nums[i], nums[j+1] = nums[j+1], nums[i]
                        break
                if not found:
                    nums[i], nums[0] = nums[0], nums[i]