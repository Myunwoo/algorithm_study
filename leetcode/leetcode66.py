class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        addOne = True
        for i in range(len(digits)-1, -1, -1):
            if not addOne:
                break

            digits[i] += 1
            if digits[i] > 9:
                digits[i] %= 10
                addOne = True
                continue    
            addOne = False
        
        if addOne:
            digits = [1] + digits
        return digits
    
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        isNeedAdd = True
        while idx > -1:
            if isNeedAdd:
                if digits[idx] < 9:
                    digits[idx] += 1
                    isNeedAdd = False
                elif digits[idx] == 9:
                    digits[idx] = 0
                    isNeedAdd = True
            idx -= 1
        
        if isNeedAdd:
            digits = [1] + digits

        return digits