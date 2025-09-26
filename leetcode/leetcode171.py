class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 문자열을 우측에서부터 순회, count++
        # 해당 문자의 값을 구함 ord(x) - ord('A') + 1
        # answer += 값 ** count

        def getVal(num):
            return ord(num) - ord('A') + 1
        
        answer = 0
        l = len(columnTitle)
        for i in range(l):
            answer += getVal(columnTitle[i]) * 26**(l-i-1)
        return answer