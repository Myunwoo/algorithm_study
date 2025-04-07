T = int(input())
for _ in range(T):
  bNum = bin(int(input()))[2:][::-1]
  arr = []
  for i in range(len(bNum)):
    if bNum[i] == '1':
      arr.append(str(i))
  print(' '.join(arr))