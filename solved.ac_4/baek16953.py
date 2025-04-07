from collections import deque

A, B = map(int, input().split())
dq = deque()
dq.append((A, 0))
answer = -1
while dq:
    cur, count = dq.popleft()
    nxt = cur*2
    if nxt == B:
        answer = count + 1
        break
    elif nxt < B:
        dq.append((nxt, count+1))
    
    nxt = cur*10 + 1
    if nxt == B:
        answer = count + 1
        break
    elif nxt < B:
        dq.append((nxt, count+1))

print(answer+1 if answer > -1 else -1)