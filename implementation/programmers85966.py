def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]
        print('i', i)
        print('have_to_deli', have_to_deli)
        print('have_to_pick', have_to_pick)

        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2
        print('answer', answer)
        print()

    return answer

print(solution(4, 5, 	[1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))