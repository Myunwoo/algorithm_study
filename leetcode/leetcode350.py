class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        answer = []
        for n in nums1:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        
        for n in nums2:
            if n in hash and hash[n]:
                answer.append(n)
                hash[n] -= 1
        return answer