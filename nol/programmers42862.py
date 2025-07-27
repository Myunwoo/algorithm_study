
def solution(n, lost, reserve):
    # lost, reserver 여분이 있지만 도둑맞은 학생을 고려해서 새로운 배열을 만든다.    
    real_lost = sorted([l for l in lost if l not in reserve])
    real_reserve = sorted([r for r in reserve if r not in lost])
    
    lostMap = {}
    for l in real_lost:
        lostMap[l] = True
    
    for r in real_reserve:
        if r-1 in lostMap and lostMap[r-1]:
            lostMap[r-1] = False
        elif r+1 in lostMap and lostMap[r+1]:
            lostMap[r+1] = False
    
    count = 0
    for l in lostMap:
        if lostMap[l]:
            count += 1
            
    
    return n - count


