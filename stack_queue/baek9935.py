#https://www.acmicpc.net/problem/9935
target=list(input())
bomb=input()
bl=len(bomb)

stack=[]
for t in target:
    stack.append(t)
    if len(stack)>=bl:
        if ''.join(stack[-bl:])==bomb:
            for _ in range(bl):
                stack.pop()

result=''.join(stack)
if result:
    print(result)
else:
    print('FRULA')