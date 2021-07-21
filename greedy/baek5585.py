#https://www.acmicpc.net/problem/5585
coins =[500,100,50,10,5,1]
cost=1000-int(input())
count=0
for coin in coins:
    if cost // coin > 0:
        count+= cost//coin
        cost-=coin*(cost//coin)
print(count)