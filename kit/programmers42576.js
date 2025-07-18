function solution(participant, completion) {
    const map = {}
    
    // O(n)
    for (const c of completion) {
        map[c] = (map[c] ?? 0) + 1
    }
    
    // O(n)
    for (const p of participant) {
        if (!map[p]) return p
        map[p]--
    }
    
    return undefined
}