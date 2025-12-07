class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ''

        while columnNumber > 0:
            columnNumber -= 1 
            answer = chr(ord('A') + columnNumber % 26) + answer
            columnNumber //= 26

        return answer

# 이 문제는 26진법 문제처럼 보이지만, 사실 0~25가 아니라 1~26인 독특한 문제.
# 따라서, 기초적인 26진법 문제처럼 불이하고자 한다면
# columnNumber -= 1 이 한 줄이 추가로 필요하다.