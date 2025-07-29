import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 수의 합을 반복적으로 구한다
        # 합이 음수이면 그 다음 수부터 다시 시작
        # 합의 최대값 도출

        curSum = 0
        answer = sys.maxsize * -1

        for num in nums:
            curSum += num
            answer = max(answer, curSum)
            if curSum < 0:
                curSum = 0
            
        return answer