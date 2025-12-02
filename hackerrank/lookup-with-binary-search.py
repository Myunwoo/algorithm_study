def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        midVal = nums[mid]
        
        if midVal == target:
            return mid
        elif midVal > target:
            right = mid - 1 # midVal이 target이냐? 를 위에서 물었기 때문에 mid는 이미 확인한 샘이다. 따라서 right는 mid-1
        elif midVal < target:
            left = mid + 1 # midVal이 target이냐? 를 위에서 물었기 때문에 mid는 이미 확인한 샘이다. 따라서 left는 mid+1
    return -1


# 이진 탐색에서는 매 반복마다 검색 구간의 길이가 절반으로 줄어듭니다.
# 따라서 검색 구간의 길이가 1이 될 때까지 필요한 반복 횟수는 대략 log2n번 입니다.
# 각 반복 내에서는 비교 연산, 인덱스 접근 정도가 발생하는 상수 시간 로직이라서,
# 이진 탐색 알고리즘의 시간 복잡도는 O(logn)입니다.


# 이진 탐색에서 값의 양/음이 중요하지 않은 이유는,
# 이진 탐색 알고리즘은 값의 정렬된 순서에 의존하기 때문이다.