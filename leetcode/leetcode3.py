class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        hash = {}
        hash[s[0]] = 0
        curIdx = 0
        answer = 0

        for i in range(1, len(s)):
            if s[i] in hash:
                curIdx = max(curIdx, hash[s[i]] + 1)
            answer = max(answer, i-curIdx+1)
            hash[s[i]] = i
        
        return answer






def lengthOfLongestSubstring(s):
    hash = {}
    answer = 0
    curIdx = 0
 
    for i in range(len(s)):
        if s[i] in hash:
            curIdx = max(curIdx, hash[s[i]] + 1)
 
        hash[s[i]] = i
        answer = max(answer, i - curIdx + 1)
 
    return answer