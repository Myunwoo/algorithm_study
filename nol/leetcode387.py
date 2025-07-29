class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}

        for ss in s:
            if ss in hash:
                hash[ss] += 1
            else:
                hash[ss] = 1
        
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i
        
        return -1