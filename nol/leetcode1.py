class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        answer = []

        for i in range(len(nums)):
            if target - nums[i] in hash:
                answer = [i, hash[target - nums[i]]]
            hash[nums[i]] = i
        return answer