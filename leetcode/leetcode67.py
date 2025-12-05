class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aIdx = len(a) - 1
        bIdx = len(b) - 1
        adding = 0

        answer = ''

        while aIdx >= 0 or bIdx >= 0 or adding > 0:
            aVal = a[aIdx] if aIdx >= 0 else 0
            bVal = b[bIdx] if bIdx >= 0 else 0

            temp = int(aVal) + int(bVal) + adding
            cur = temp % 2
            adding = temp // 2

            answer += str(cur)

            aIdx -= 1
            bIdx -= 1
        

        return ''.join(reversed(answer))