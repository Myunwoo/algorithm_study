class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        
        answer = [0 for _ in range(len(temperatures))]
        stack = []
        stack.append([temperatures[0], 0])

        for i in range(1, len(temperatures)):
            if stack[-1][0] < temperatures[i]:
                while stack:
                    if stack[-1][0] >= temperatures[i]:
                        break
                    temp, idx = stack.pop()
                    answer[idx] = i - idx
            stack.append([temperatures[i], i])
        return answer
