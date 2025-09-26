class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        idx = 0
        while True:
            cur = 3**idx
            if cur == n:
                return True
            elif cur > n:
                return False
            else:
                idx += 1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 3:
            return False
        
        def recursion(n):
            if n == 1:
                return True
            if n % 3 != 0:
                return False
            return recursion(n//3)
        return recursion(n)