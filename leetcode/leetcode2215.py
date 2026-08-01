class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        m1, m2 = {}, {}
        ret1, ret2 = [], []
        for n1 in nums1:
            m1[n1] = True
        for n2 in nums2:
            m2[n2] = True

        for k1 in m1.keys():
            if k1 not in m2:
                ret1.append(k1)
        
        for k2 in m2.keys():
            if k2 not in m1:
                ret2.append(k2)
        
        return [ret1, ret2]