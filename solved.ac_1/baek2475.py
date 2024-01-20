i = input()
arr = i.split()
print(sum([int(a)**2 for a in arr])%10)