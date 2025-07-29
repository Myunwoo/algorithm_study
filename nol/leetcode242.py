class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def getOrd(c):
            return ord(c) - ord('a')

        arr = [0] * 26

        for ss in s:
            arr[getOrd(ss)] += 1
        for tt in t:
            arr[getOrd(tt)] -= 1
            if arr[getOrd(tt)] < 0:
                return False

        return True