import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = sys.maxsize
        answer = -1
        for i in range(len(prices)):
            m = min(m, prices[i])
            answer = max(answer, prices[i] - m)
        return answer