class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []      # 인덱스를 저장하는 스택
        water = 0

        for i, h in enumerate(height):
            # 현재 기둥이 스택 top보다 크면, 물이 고일 수 있는 오른쪽 벽이 된 것
            while stack and h > height[stack[-1]]:
                mid = stack.pop()  # 가운데(바닥)가 될 기둥 인덱스

                if not stack:
                    # 왼쪽 벽이 없으면 물 못 고임
                    break

                left = stack[-1]  # 왼쪽 벽 인덱스
                # 양쪽 벽 중 더 낮은 높이 - 바닥 높이 = 물 높이
                bounded_height = min(height[left], h) - height[mid]
                # 폭: 왼쪽/오른쪽 벽 사이의 칸 수
                width = i - left - 1

                water += bounded_height * width

            # 현재 기둥을 스택에 넣어서, 이후 오른쪽에서 더 큰 벽을 기다림
            stack.append(i)

        return water
