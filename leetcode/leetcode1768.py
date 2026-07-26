class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1 = 0
        idx2 = 0
        ret = ''

        while idx1 < len(word1) and idx2 < len(word2):
            ret += word1[idx1] + word2[idx2]
            idx1 += 1
            idx2 += 1
        
        if idx1 != len(word1):
            ret += word1[idx1:]
        elif idx2 != len(word2):
            ret += word2[idx2:]
        
        return ret