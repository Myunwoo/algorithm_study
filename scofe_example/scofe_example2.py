import sys

T = int(sys.stdin.readline().strip())

counts = []

for _ in range(T):
    count = 0
    #N=한정, M=일반
    N, M = map(int, sys.stdin.readline().strip().split())

    n_set = N // 5
    if n_set == 0:
        counts.append(count)
        continue
    m_set = M // 7
    #아름다운 한 세트의 개수
    full_set = min(n_set,m_set)
    count += full_set

    N -= full_set * 5
    M -= full_set * 7

    #한정 쿠폰 12개로 만들 수 있는 커피의 개수
    full_set = (N // 12)
    count += full_set
    N -= full_set * 12

    #남아있는 한정 쿠폰이 5개 이상일 경우에 일반 쿠폰을 더해 12개를 채울 수 있다면, 한 잔 더 만들고 끝
    if N >= 5 and (12-N) <= M:
        count += 1

    counts.append(count)


for c in counts:
    print(c)