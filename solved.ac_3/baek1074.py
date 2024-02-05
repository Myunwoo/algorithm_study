import sys
N, r, c = list(map(int, sys.stdin.readline().split()))

def find(N, r, c):
  if N == 1:
    if r == 0 and c == 0:
      return 0
    elif r == 0 and c == 1:
      return 1
    elif r == 1 and c == 0:
      return 2
    elif r == 1 and c == 1:
      return 3
  div = 2**(N-1)
  if r < div and c < div:
    return find(N-1, r, c)
  elif r < div and c >= div:
    return find(N-1, r, c-div) + (2**(N-1))*(2**(N-1))
  elif r >= div and c < div:
    return find(N-1, r-div, c) + (2**(N-1))*(2**(N-1))*2
  elif r >= div and c >= div:
    return find(N-1, r-div, c-div) + (2**(N-1))*(2**(N-1))*3
  
print(find(N, r, c))