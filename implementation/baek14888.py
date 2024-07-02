import sys

N = int(input())
nums = list(map(int, input().split()))
operands = list(map(int, input().split()))

maxV = -sys.maxsize
minV = sys.maxsize

def calc(curIdx, curVal, plus, minus, mul, div):
    global maxV, minV, N
    if curIdx == N:
        maxV = max(maxV, curVal)
        minV = min(minV, curVal)
        return
    if plus > 0:
        calc(curIdx+1, curVal+nums[curIdx], plus-1, minus, mul, div)
    if minus > 0:
        calc(curIdx+1, curVal-nums[curIdx], plus, minus-1, mul, div)
    if mul > 0:
        calc(curIdx+1, curVal*nums[curIdx], plus, minus, mul-1, div)
    if div > 0:
        calc(curIdx+1, int(curVal/nums[curIdx]), plus, minus, mul, div-1)

calc(1, nums[0], operands[0], operands[1], operands[2], operands[3])
print(maxV)
print(minV)