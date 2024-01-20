word = input()

for i in range(97, 123):
  c = chr(i)
  print(word.index(c) if c in word else -1, end=' ' if i != 122 else '')