import sys

N = int(input())

positives = []
ones = []
others = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 1:
        positives.append(num)
    elif num == 1:
        ones.append(num)
    else:
        others.append(num)

positives.sort(reverse=True)
others.sort()

def sumOfArr(arr):
    result = 0
    isOdd = True
    if len(arr) % 2 == 0:
        isOdd = False

    i=0
    for _ in range(len(arr) // 2):
        result += arr[i] * arr[i+1]
        i+=2
            
    #홀수면 마지막 요소가 있을거고, 짝수면 없을거니까 끝내면됨.
    if isOdd == True:
        result += arr[len(arr)-1]
    
    return result

#1인 경우에 곱하면 안된다는걸 처음엔 몰랐음...!
def sumOfOnes(arr):
    result = 0
    for a in arr:
        result += a

    return result


print(sumOfArr(positives) + sumOfArr(others) + sumOfOnes(ones))