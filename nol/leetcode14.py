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

