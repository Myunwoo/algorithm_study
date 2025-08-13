class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1 if j == 0 or j == i else 0 for j in range(i+1)] for i in range(numRows)]
        
        if numRows < 3:
            return answer
        
        for i in range(2, numRows):
            for j in range(1, len(answer[i])-1):
                answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
        return answer