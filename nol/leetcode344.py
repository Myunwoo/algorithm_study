class Solution:
    def reverseString(self, s: List[str]) -> None:
        idx = len(s) // 2

        for i in range(idx):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]