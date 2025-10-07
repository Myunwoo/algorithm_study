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