class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        num = 1
        for i in range(n, 0, -1):
            num *= i
        answer = 0

        while True:
            if num % 10 == 0:
                answer+=1
                num //= 10
            else:
                break
        return answer