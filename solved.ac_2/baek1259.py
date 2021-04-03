#https://www.acmicpc.net/problem/1259

import copy

results = []

while True:
    num = list(input())
    if num[0] == '0':
        break

    palindrome = copy.deepcopy(num)

    count = 0
    isPalindrome = True

    while palindrome:
        if num[count] != palindrome.pop():
            isPalindrome = False
            break
        count += 1

    if isPalindrome == True:
        results.append("yes")
    else:
        results.append("no")

for result in results:
    print(result)