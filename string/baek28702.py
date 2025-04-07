a = input()
b = input()
c = input()

arr = [a, b, c]
idx = 0
for i in range(len(arr)):
    if arr[i].isnumeric():
        idx = i

target = int(arr[idx]) + (3-idx)

if target % 3 == 0 and target % 5 != 0:
    print('Fizz')
elif target % 3 != 0 and target % 5 == 0:
    print('Buzz')
elif target % 3 == 0 and target % 5 == 0:
    print('FizzBuzz')
else:
    print(target)