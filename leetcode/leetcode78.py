class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  # 빈 집합 포함

        for num in nums:
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [num])
            result += new_subsets
        
        return result
