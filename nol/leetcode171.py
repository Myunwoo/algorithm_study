class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def getOrd(s):
            return ord(s) - ord('A') + 1
        answer = 0
        for i in range(len(columnTitle)-1, -1, -1):
            answer += (26**(len(columnTitle)-1-i)) * getOrd(columnTitle[i])
        return answer