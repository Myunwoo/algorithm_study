class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        for i in range(l//2):
            s[i], s[l-1-i] = s[l-1-i], s[i]