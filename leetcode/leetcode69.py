def mySqrt(x: int) -> int:
        answer = 0

        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            double = mid * mid
            if double == x:
                return mid
            elif double > x:
                left = mid + 1
            elif double < x:
                right = mid - 1

mySqrt(8)


def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # 0 또는 1은 자기 자신이 제곱근

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right  # 반복문 종료 시 right가 정답 (가장 큰 제곱근)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        for i in range(1,x+1):
            v = i * i
            if v > x:
                return i - 1
            elif v == x:
                return i