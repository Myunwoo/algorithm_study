class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        isNegative = True if x < 0 else False
        if isNegative:
            x *= -1
        
        while x > 0:
            answer *= 10
            answer += x % 10
            x //= 10
        
        if isNegative:
            answer *= -1

        return answer if -1 * 2**31 <= answer <= 2**31 - 1 else 0