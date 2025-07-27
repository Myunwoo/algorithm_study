class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums)//2
        answer = -1
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
            
            if dic[num] > target:
                answer = num
                break

        return answer