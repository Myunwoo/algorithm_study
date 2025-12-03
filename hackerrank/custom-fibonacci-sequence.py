def getAutoSaveInterval(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    
    arr = [0 for _ in range(n+1)]
    arr[0] = 1
    arr[1] = 2
    
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]



# 공간 복잡도를 O(1)로 개선한 풀이
# 모든 수의 합을 저장할 필요가 없고, 한 칸 전과 두 칸 전의 값만 알면 되기 때문임.
def getAutoSaveInterval(n):
    if n == 0:
        return 1
    if n == 1:
        return 2

    prev2 = 1  # F(0)
    prev1 = 2  # F(1)

    for _ in range(2, n + 1):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur

    return prev1
