expressions = input().split('-')

result =0

first_members = expressions[0].split('+')

for member in first_members:
    result += int(member)

for i in range(1, len(expressions)):
    second_members = expressions[i].split('+')
    for member in second_members:
        result -= int(member)

print(result)