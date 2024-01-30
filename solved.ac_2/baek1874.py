import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
num = []
answer = []
count = 1

for a in arr:
    if not num:
        num.append(count)
        count += 1
        answer.append('+')
        continue
    if num[-1] > a:
        answer = ['NO']
        break
    while num[-1] < a:
        num.append(count)
        count += 1
        answer.append('+')
    num.pop()
    answer.append('-')
            
    print('num', num)
    print('answer', answer)