class Solution:
    def isHappy(self, n: int) -> bool:
        hash = {}

        while n != 1:
            if n in hash:
                return False
            hash[n] = True
            newNum = 0
            while n != 0:
                newNum += (n % 10)**2
                n //= 10
            n = newNum
        
        return True
    

class Solution:
    def isHappy(self, n: int) -> bool:
        hash = {}

        while n != 1:
            if n in hash:
                return False
            hash[n] = True
            curN = n
            temp = 0
            while curN > 0:
                temp += (curN % 10) ** 2
                curN //= 10
            n = temp
        
        return True