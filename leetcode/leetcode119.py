class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0 for _ in range(rowIndex+1)]
        row[0] = 1

        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                l, r = row[j-1], row[j]
                row[j] = l + r

        return row
    
# 파스칼 삼각형의 마지막 행만큼의 공간 복잡도를 가지게 풀어내는 방법
# 뒤에서부터 순회 (for j in range(i, 0, -1):)가 핵심이다.
# 앞에서부터 순회하면 누적이되어 답이 나올 수 없음