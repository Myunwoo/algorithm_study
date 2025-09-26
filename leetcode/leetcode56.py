class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: [x[0], x[1]])
        answer = []

        answer.append(intervals[0])

        for i in range(1, len(intervals)):
            if answer[-1][1] >= intervals[i][0]:
                answer[-1] = [min(answer[-1][0], intervals[i][0]), max(answer[-1][1], intervals[i][1])]
            else:
                answer.append(intervals[i])
        
        return answer