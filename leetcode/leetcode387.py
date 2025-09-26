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
    

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        answer = -1
        for i in range(len(s)):
            if s[i] in hash:
                hash[s[i]][0] = False
            else:
                hash[s[i]] = [True, i]
        
        for k in hash.keys():
            if hash[k][0]:
                answer = hash[k][1]
                break
        return answer