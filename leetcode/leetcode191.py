class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        answer = 0

        for num in n:
            if num == '1':
                answer += 1
        return answer