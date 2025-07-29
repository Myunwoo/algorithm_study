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
    


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        ansArr = [nums[0], 1]

        for i in range(1, len(nums)):
            if nums[i] == ansArr[0]:
                ansArr[1] += 1
            else:
                ansArr[1] -= 1
                if ansArr[1] == 0:
                    ansArr[0] = nums[i]
                    ansArr[1] = 1
        
        return ansArr[0]