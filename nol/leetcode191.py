class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        bNum = bin(n)[2:]
        for n in bNum:
            if n == '1':
                answer += 1
        return answer