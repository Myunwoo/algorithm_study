#https://www.acmicpc.net/problem/16120
word=list(input())

stack=[]
ppap=['P','P','A','P']
for i in word:
    stack.append(i)
    if stack[-4:]==ppap:
        for _ in range(4):
            stack.pop()
        stack.append('P')

if stack==ppap or stack==['P']:
    print('PPAP')
else:
    print('NP')