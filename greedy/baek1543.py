#https://www.acmicpc.net/problem/1543
word=list(input())
target=input()

word=list(reversed(word))

stack=''
count=0
while word:
    stack+=word.pop()
    try:
        stack.index(target)
    except ValueError:
        continue
    count+=1
    stack=''

print(count)