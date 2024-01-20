a = int(input())
b = int(input())
c = int(input())

d = str(a*b*c)
dic = {
  '0':0,
  '1':0,
  '2':0,
  '3':0,
  '4':0,
  '5':0,
  '6':0,
  '7':0,
  '8':0,
  '9':0,
}

for dd in d:
  dic[dd] += 1

for key in dic:
  print(dic[key])