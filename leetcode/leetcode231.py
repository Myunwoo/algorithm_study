class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
    
# 2의 제곱수는 이진수로 표현했을떄 항상 1이 하나만 존재한다.
# 이때, 그 수의 -1은 모두 1로 이루어진 수가 된다.
# 예시) 100, 11는 각각 4,3이다.
# 4 & 3 은 겹치는 1이 없다.