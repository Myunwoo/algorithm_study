class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = {}

        for ss in s:
            if ss in hash:
                hash[ss] += 1
            else:
                hash[ss] = 1
        
        for tt in t:
            if tt in hash:
                hash[tt] -= 1
                if hash[tt] == -1:
                    return False
            else:
                return False
        
        return True