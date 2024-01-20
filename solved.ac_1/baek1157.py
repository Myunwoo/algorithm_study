from collections import Counter

inputString = input()
inputString = inputString.upper()
t = Counter(inputString).most_common()

if len(t) > 1 and t[0][1] == t[1][1]:
  print('?')
else:
  print(t[0][0])