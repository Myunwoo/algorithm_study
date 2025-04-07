def solution(s, skip, index):
    answer = ''
    skip = set(skip)
    words = list(s)
    for i in range(len(words)):
        cur = words[i]
        count = index
        while count > 0:
            cur = chr(ord(cur)+1)
            if ord(cur) > 122:
                cur = chr(ord(cur)-26)
            if cur not in skip:
                count -= 1
        words[i] = cur
    answer = ''.join(words)
    return answer