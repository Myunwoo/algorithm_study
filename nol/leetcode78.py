class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(start, cur):
            answer.append(cur[:])  # 부분 집합 저장
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()
        
        backtrack(0, [])
        return answer
