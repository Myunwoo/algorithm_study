class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        answer = []

        for i in range(len(nums)):
            if target - nums[i] in hash:
                answer = [i, hash[target - nums[i]]]
            hash[nums[i]] = i
        return answer
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
            
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        nums.sort()

        while l < r:
            curVal = nums[l][0] + nums[r][0]
            if curVal > target:
                r -= 1
            elif curVal < target:
                l += 1
            elif curVal == target:
                break
        return [nums[l][1], nums[r][1]]