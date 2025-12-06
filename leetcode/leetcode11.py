class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 넓이를 구하는 공식은 min(height[i], height[j]) * (j - i)
        # i와j가 가까워질 수록 숫자가 감소하는 구조.
        # 그럼 min(height[i], height[j])가 커지는 것에 기대를 걸어보아야 한다.
        # 따라서 heigh[i], height[j] 중, 작은 쪽을 움직여보자.
        answer = -1
        left,right = 0, len(height)-1
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            answer = max(answer, w*h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer