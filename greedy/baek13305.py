city_count = int(input())
road_lengths = list(map(int, input().split()))
oil_costs = list(map(int, input().split()))

cheapest_oil = oil_costs[0]

result = 0

for i in range(len(road_lengths)):
    if cheapest_oil > oil_costs[i]:
        cheapest_oil = oil_costs[i]
        result += cheapest_oil * road_lengths[i]
    else:
        result += cheapest_oil * road_lengths[i]


print(result)