def make(path, opened, closed, n, answer):
    if opened == n and closed == n:
        answer.append(path)
        return
    
    if opened < n:
        make(path+'<', opened+1, closed, n, answer)
    if closed < n and opened > closed:
        make(path+'>', opened, closed+1, n, answer)

def generateAngleBracketSequences(n):
    answer = []
    make('', 0, 0, n, answer)
    return answer
    