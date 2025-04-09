import sys

N = int(sys.stdin.readline())
PS, PE = list(sys.stdin.readline().strip().split('*'))
files = [sys.stdin.readline().strip() for _ in range(N)]

for f in files:
    if not f.startswith(PS):
        print('NE')
        continue
    f = f[len(PS):len(f)]
    if not f.endswith(PE):
        print('NE')
        continue
    print('DA')