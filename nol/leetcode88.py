class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        maxIdx = m + n - 1
        n1Idx = m - 1
        n2Idx = n - 1

        while True:
            if n1Idx >= 0 and n2Idx >= 0:
                if nums1[n1Idx] > nums2[n2Idx]:
                    nums1[maxIdx], nums1[n1Idx] = nums1[n1Idx], nums1[maxIdx]
                    maxIdx -= 1
                    n1Idx -= 1
                else:
                    nums1[maxIdx] = nums2[n2Idx]
                    maxIdx -= 1
                    n2Idx -= 1
            elif n1Idx >= 0 and n2Idx < 0:
                nums1[maxIdx], nums1[n1Idx] = nums1[n1Idx], nums1[maxIdx]
                maxIdx -= 1
                n1Idx -= 1
            elif n1Idx < 0 and n2Idx >= 0:
                nums1[maxIdx] = nums2[n2Idx]
                maxIdx -= 1
                n2Idx -= 1
            else:
                break