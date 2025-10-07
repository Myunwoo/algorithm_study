import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        answer = -sys.maxsize
        for num in nums:
            curSum += num
            answer = max(answer, curSum)

            if curSum < 0:
                curSum = 0
        
        return answer