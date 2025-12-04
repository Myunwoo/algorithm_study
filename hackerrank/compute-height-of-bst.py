def getBinarySearchTreeHeight(values, leftChild, rightChild):
    n = len(values)
    if n == 0:
        return 0

    sys.setrecursionlimit(10**6)

    def height(idx: int) -> int:
        if idx == -1:
            return 0

        lh = height(leftChild[idx])
        rh = height(rightChild[idx])
        
        return 1 + max(lh, rh)

    return height(0)

# value에 노드의 값, leftChild에 왼쪽 자식, rightChild에 오른쪽 자식이 "인덱스기반"으로 주어지는 문제.
# head가 0번째 인덱스로 고정되어 있는 상황에서, 0번째 인덱스 기준 depth를 구한다.
# 노드 형태가 아니라 이렇게도 트리가 제공될 수 있구나...