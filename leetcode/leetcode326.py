class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        def recursion(num):
            if num == 1:
                return True
            elif num % 3 == 0:
                return recursion(num // 3)
            else:
                return False

        return recursion(n)