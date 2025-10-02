class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        num = bin(n)[2:]
        num = '0'*(32-len(num)) + num

        for i in range(31, -1, -1):
            if num[i] == '1':
                answer += 2**i

        return answer
