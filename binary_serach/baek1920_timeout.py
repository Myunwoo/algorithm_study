#https://www.acmicpc.net/problem/1920

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int,input().split()))

def binary_search(arr, target):
    if len(arr) == 1:
        if arr[0] == target:
            return True
        else:
            return False

    index = len(arr) // 2
    if target > arr[index]:
        print(arr[index:])
        return binary_search(arr[index:],target)
    elif target == arr[index]:
        return True
    else:
        print(arr[:index])
        return binary_search(arr[:index],target)

for b in B:
    result = binary_search(A,b)
    if result == True:
        print(1)
    else:
        print(0)