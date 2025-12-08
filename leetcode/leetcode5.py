class Solution:
    def longestPalindrome(self, s: str) -> str:
        def lookup(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        if len(s) <= 1 or s == s[::-1]: return s
        ans = ''
        for i in range(len(s)-1):
            ans = max(ans, lookup(s, i, i+1), lookup(s, i, i+2), key=len)
        return ans


# 아래는 내가 푼 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        def checkEven(idx1, idx2, s):
            left, right = idx1, idx2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        def checkOdd(idx, s):
            left, right = idx, idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        # 팰린드롬의 특성을 활용해서, 모든 인덱스를 중심으로 간주하고, 확장해 나가는 풀이
        answer = []
        for i in range(len(s)):
            answer = max(answer, checkEven(i, i+1, s), checkOdd(i, s), key=len)
        return answer