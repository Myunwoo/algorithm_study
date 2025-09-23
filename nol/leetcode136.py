class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR 누적
        return result
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        for n in nums:
            if n in hash:
                del hash[n]
            else:
                hash[n] = True
        
        for i in hash.keys():
            return i