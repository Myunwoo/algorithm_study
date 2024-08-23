def solution(numbers, hand):
    answer = ''
    dic = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1]
    }
    left = [3, 0]
    right = [3, 2]
    
    for n in numbers:
        if n in [1, 4, 7]:
            left = dic[n]
            answer += 'L'
        elif n in [3, 6, 9]:
            right = dic[n]
            answer += 'R'
        else:
            if abs(dic[n][0]-left[0])+abs(dic[n][1]-left[1]) > abs(dic[n][0]-right[0])+abs(dic[n][1]-right[1]):
                right = dic[n]
                answer += 'R'
            elif abs(dic[n][0]-left[0])+abs(dic[n][1]-left[1]) < abs(dic[n][0]-right[0])+abs(dic[n][1]-right[1]):
                left = dic[n]
                answer += 'L'
            else:
                if hand == 'left':
                    left = dic[n]
                    answer += 'L'
                else:
                    right = dic[n]
                    answer += 'R'
    return answer