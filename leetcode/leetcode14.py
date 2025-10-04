class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[len(strs)-1]

        if not first or not last:
            return ''

        answer = ''
        idx = 0
        while True:
            if idx >= len(first) or idx >= len(last):
                break
            if first[idx] !=  last[idx]:
                break
            answer += first[idx]
            idx += 1

        return answer

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        for i in range(1, len(strs)):
            curAnswer = ''
            l = min(len(answer), len(strs[i]))

            for j in range(l):
                if strs[i][j] != answer[j]:
                    break
                curAnswer += answer[j]
            answer = curAnswer
        return answer