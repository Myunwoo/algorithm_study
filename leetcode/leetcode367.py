class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, 2**16
        while left <= right:
            mid = left + (right-left) // 2
            cur = mid * mid

            if cur == num:
                return True
            elif cur < num:
                left = mid + 1
            elif cur > num:
                right = mid - 1
        return False
    
# sqrt를 사용하지 않고, 어떠한 수가 다른 어떤 수의 제곱인지 확인하는 법
# 이것도 이분탐색 유형이네. 범위 내에서 찾는거니까.
# 아무튼간 찾을 때 이분탐색 해보면 좋음.