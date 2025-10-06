class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        arr = [True for _ in range(n+1)]
        arr[0] = False
        arr[1] = False

        for i in range(2, int(n**0.5)+1):
            if arr[i]:
                idx = 2
                while i * idx < n+1:
                    arr[i * idx] = False
                    idx += 1
        answer = 0
        for i in range(n):
            if arr[i]:
                answer += 1
        return answer