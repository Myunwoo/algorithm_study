def solution(n, lost, reserve):
    # 변수의 재사용에 대해 고민좀 할 것.
    real_lost = sorted([l for l in lost if l not in reserve])
    real_reserve = sorted([r for r in reserve if r not in lost])
    count = 0

    lostMap = {l: True for l in real_lost}

    for r in real_reserve:
        if r - 1 in lostMap and lostMap[r - 1]:
            lostMap[r - 1] = False
            count += 1
            continue

        if r + 1 in lostMap and lostMap[r + 1]:
            lostMap[r + 1] = False
            count += 1

    return n - len(real_lost) + count
