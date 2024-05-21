A, B, C = map(int, input().split())

arr = [A**i%C for i in range(1, 11)]
print(arr[C%10])
