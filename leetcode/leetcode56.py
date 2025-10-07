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

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:[x[0], -x[1]])
        
        idx = 0

        while idx < len(intervals) - 1:
            if intervals[idx][1] >= intervals[idx+1][0]:
                intervals[idx+1] = [min(intervals[idx][0], intervals[idx+1][0]), max(intervals[idx][1], intervals[idx+1][1])]
                intervals.remove(intervals[idx])
            else:
                idx += 1
        
        return intervals
                
