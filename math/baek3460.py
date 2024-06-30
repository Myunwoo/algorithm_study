T = int(input())
for _ in range(T):
  num = int(input())
  bNum = bin(num)[2:][::-1]
  arr = []
  for i in range(len(bNum)):
    if bNum[i] == '1':
      arr.append(i)
  for i in range(len(arr)):
    if i < len(arr)-1:
      print(arr[i], end=' ')
    else:
      print(arr[i])